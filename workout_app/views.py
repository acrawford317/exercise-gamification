from django.shortcuts import render
import requests
from django.views import generic
# from django.views.generic import CreateView, ListView
# from .models import Workout
# from .forms import WorkoutForm

from .forms import WorkoutTypeForm, WorkoutLinkedForm, WorkoutTypeCountForm, CityForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import WorkoutLinked
from django.forms.models import model_to_dict
from .models import WorkoutType
from datetime import datetime, timedelta
from measurement.measures import Distance, Weight
from .models import WorkoutTypeCount
import m26

from .models import Achievement
from .models import Profile
from .models import City
from django.template.defaultfilters import pluralize

import datetime

import pgeocode

LE = 'Please login before viewing or submitting this'

def index(request):
    context = {}
    return render(request, 'workout_app/index.html', context)

def ensure_profile(user_te):
    try:
        user_profile = user_te.profile
    except:
        new_profile = Profile(user = user_te)
        new_profile.save()

# class AddWorkoutView(CreateView):
#     model = Workout
#     from_class = WorkoutForm
#     template_name = 'workout_app/add_workout.html'
#     fields = '__all__'

# class WorkoutListView(generic.ListView):
#     model = Workout
#     object_list = Workout.objects.all()
#     template_name = 'workout_app/workout_list.html'
#     fields = '__all__'

def achievementEarned(achivement, workouts):
    tf = workouts.all()
    if achivement.has_start_date:
        tf_temp = tf.filter(start_date__gte = achivement.start_date, one_day = True)
        tf = tf_temp | tf.filter(end_date__gte = achivement.start_date, one_day = False)
    if achivement.has_end_date:
        tf = tf.filter(start_date__lte = achivement.end_date)
    if achivement.has_specific_workoutType:
        if achivement.has_second_specific_workoutType:
            tf = tf.filter(workoutType__in = [achivement.specific_workoutType, achivement.second_specific_workoutType])
        else:
            tf = tf.filter(workoutType = achivement.specific_workoutType)
    if achivement.has_workout_count_min:
        if tf.count() < achivement.workout_count_min:
            return False
    if achivement.has_specific_WorkoutTypeCount:
        spec_count = 0
        for wo in tf.filter(workoutType__has_first_count_component = True, workoutType__first_count_component = achivement.specific_WorkoutTypeCount):
            spec_count += wo.raw_count
        for wo in tf.filter(workoutType__has_second_count_component = True, workoutType__second_count_component = achivement.specific_WorkoutTypeCount):
            spec_count += wo.second_raw_count
        if spec_count < achivement.specific_WorkoutTypeCount_min:
            return False
    if achivement.has_second_specific_WorkoutTypeCount:
        spec_count = 0
        for wo in tf.filter(workoutType__has_first_count_component = True, workoutType__first_count_component = achivement.second_specific_WorkoutTypeCount):
            spec_count += wo.raw_count
        for wo in tf.filter(workoutType__has_second_count_component = True, workoutType__second_count_component = achivement.second_specific_WorkoutTypeCount):
            spec_count += wo.second_raw_count
        if spec_count < achivement.second_specific_WorkoutTypeCount_min:
            return False
    if achivement.has_min_single_weight:
        satis = False
        for wo in tf.filter(workoutType__has_weight_comp = True):
            if wo.weight >= achivement.min_single_weight:
                satis = True
                break
        if not satis:
            return False
    if achivement.has_min_total_weight:
        weight_tot = Weight()
        for wo in tf.filter(workoutType__has_weight_comp = True, workoutType__has_set_rep_comp = False):
            weight_tot += wo.weight
        for wo in tf.filter(workoutType__has_weight_comp = True, workoutType__has_set_rep_comp = True):
            weight_tot += (wo.raw_set * wo.raw_rep * wo.weight)
        if weight_tot < achivement.min_total_weight:
            return False
    if achivement.has_min_reps:
        reps_tot = 0
        for wo in tf.filter(workoutType__has_set_rep_comp = True):
            reps_tot += (wo.raw_set * wo.raw_rep)
        if reps_tot < achivement.min_reps:
            return False
    if achivement.has_min_single_distance:
        satis = False
        for wo in tf.filter(workoutType__has_distance_comp = True):
            if wo.dist >= achivement.min_single_distance:
                satis = True
                break
        if not satis:
            return False
    if achivement.has_min_total_distance:
        dist_tot = Distance()
        for wo in tf.filter(workoutType__has_distance_comp = True):
            dist_tot += wo.dist
        if dist_tot < achivement.min_total_distance:
            return False
    if achivement.has_min_single_duration:
        satis = False
        for wo in tf.filter(workoutType__has_duration = True):
            if wo.duration >= achivement.min_single_duration:
                satis = True
                break
        if not satis:
            return False
    if achivement.has_min_total_duration:
        dur_tot = timedelta()
        for wo in tf.filter(workoutType__has_duration = True):
            dur_tot += wo.duration
        if dur_tot < achivement.min_total_duration:
            return False
    if achivement.has_max_pace:
        tf_temp = tf.filter(workoutType__has_distance_comp = True, workoutType__has_duration = True)
        if achivement.has_min_single_duration:
            tf_temp = tf_temp.filter(duration__gte = achivement.min_single_duration)
        if achivement.has_min_single_distance:
            tf_temp = tf_temp.filter(dist__gte = achivement.min_single_distance)
        satis = False
        for wo in tf_temp:
            m26d = m26.Distance(wo.dist.mi)
            m26t = m26.ElapsedTime(int(wo.duration.total_seconds()))
            m26s = m26.Speed(m26d, m26t)
            try:
                t = datetime.strptime(m26s.pace_per_mile(),"%M:%S.%f")
                if timedelta(hours=t.hour, minutes=t.minute, seconds=t.second) <= achivement.max_pace_per_mile:
                    satis = True
                    break
            except:
                pass # divide by zero for Pace per mile
        if not satis:
            return False
    return True

def achievementsView(request):
    if request.user.is_anonymous:
        messages.error(request, LE)
        return HttpResponseRedirect('/login/')
    ensure_profile(request.user)
    user_workouts = WorkoutLinked.objects.filter(profile=request.user)
    context = {}
    # context['achievements_calc'] = [(a, achievementEarned(a, user_workouts)) for a in Achievement.objects.all()]
    context['achievements_calc'] = []
    context['total_possible_points'] = 0
    context['total_earned_points'] = 0
    context['total_missed_points'] = 0
    context['total_possible_achievement_num'] = 0
    context['total_earned_achievement_num'] = 0
    context['total_missed_achievement_num'] = 0
    for a in Achievement.objects.all():
        context['total_possible_points'] += a.points
        context['total_possible_achievement_num'] += 1
        if achievementEarned(a, user_workouts):
            context['achievements_calc'].append((a, True))
            context['total_earned_points'] += a.points
            context['total_earned_achievement_num'] += 1
        else:
            context['achievements_calc'].append((a, False))
            context['total_missed_points'] += a.points
            context['total_missed_achievement_num'] += 1
    # context['point_delta'] = context['total_earned_points'] - request.user.profile.achievement_points
    point_delta = context['total_earned_points'] - request.user.profile.achievement_points
    if point_delta > 0:
        messages.info(request, ("You've gained {pi} point" + pluralize(point_delta) + " since last checking your achievements").format(pi = point_delta))
    elif point_delta < 0:
        messages.info(request, ("You've lost {pi} point" + pluralize(-1 * point_delta) + " since last checking your achievements").format(pi = -1 * point_delta))
    achievement_num_delta = context['total_earned_achievement_num'] - request.user.profile.achievement_num
    if achievement_num_delta > 0:
        messages.info(request, ("You've gained {pi} achievement" + pluralize(achievement_num_delta) + " since last checking your achievements").format(pi = achievement_num_delta))
    elif achievement_num_delta < 0:
        messages.info(request, ("You've lost {pi} achievement" + pluralize(-1 * achievement_num_delta) + " since last checking your achievements").format(pi = -1 * achievement_num_delta))
    request.user.profile.achievement_points = context['total_earned_points']
    request.user.profile.achievement_num = context['total_earned_achievement_num']
    request.user.profile.save()
    return render(request, 'workout_app/achievements.html', context)

def workoutLinkedListView(request):
    if request.user.is_anonymous:
        messages.error(request, LE)
        return HttpResponseRedirect('/login/')
    user_workouts = WorkoutLinked.objects.filter(profile=request.user).order_by('-start_date')

    if (request.GET.get('WeatherButton')):
        current_workout = WorkoutLinked.objects.get(id=request.GET.get('WeatherButton'))
        y = int(current_workout.get_year())
        m = int(current_workout.get_month())
        d = int(current_workout.get_day())
        start = str(int(datetime.datetime(y, m, d, 12, 0, 0).timestamp()))
        end = str(int(datetime.datetime(y, m, d, 12, 0, 0).timestamp()))

        # city = 'charlottesville'

        # url = 'http://history.openweathermap.org/data/2.5/history/city?q=' + city + ',us&type=hour&start=' + start + '&end=' + end + '&units=imperial&appid=4b11880620bbfa64946645fe86d99eb5'

        nomi = pgeocode.Nominatim('us')
        postal_query = nomi.query_postal_code(current_workout.zipcode)
        lat = str(postal_query.latitude)
        lon = str(postal_query.longitude)

        url = 'http://history.openweathermap.org/data/2.5/history/city?lat=' + lat + '&lon=' + lon + '&type=hour&start=' + start + '&end=' + end + '&units=imperial&appid=4b11880620bbfa64946645fe86d99eb5'

        city_weather = requests.get(url).json()

        weather_info = {
            'city': postal_query.place_name,
            'temperature': "{0:.2f}".format( 1.8 * (city_weather['list'][0]['main']['temp'] - 273) + 32 ),
            'description': city_weather['list'][0]['weather'][0]['description'],
            'icon': city_weather['list'][0]['weather'][0]['icon']
        }
        context = {'weather_info': weather_info, 'current_workout': current_workout}
        return render(request, 'workout_app/workout_weather.html', context)

    if (request.GET.get('DeleteButton')):
        WorkoutLinked.objects.filter(id=request.GET.get('DeleteButton')).delete()
        return render(request, 'workout_app/workout_linked_list.html', {'user_workouts': user_workouts})

    if (request.GET.get('EditButton')):
        current_workout = WorkoutLinked.objects.get(id=request.GET.get('EditButton'))

        if request.method == 'POST':
            form = WorkoutLinkedForm(request.POST, instance = current_workout)
            if form.is_valid():
                ots = form.save(commit=False)
                ots.profile = request.user
                ots.save()
                return HttpResponseRedirect('/workout_linked_list/')
        else:
            form = WorkoutLinkedForm(initial = model_to_dict(current_workout))
        return render(request, 'workout_app/edit_workout_linked.html', {'form': form})

    return render(request, 'workout_app/workout_linked_list.html', {'user_workouts': user_workouts})

def workoutSummary(request):
    if request.user.is_anonymous:
        messages.error(request, LE)
        return HttpResponseRedirect('/login/')
    context = {}
    context['wts'] = {}
    context['cts'] = {}
    user_workouts = WorkoutLinked.objects.filter(profile=request.user)
    for wt in WorkoutType.objects.all():
        woct = user_workouts.filter(workoutType=wt)
        if woct:
            dur_tot = timedelta()
            dist_tot = Distance()
            weight_tot = Weight()
            context['wts'][wt] = []
            if wt.has_duration:
                for iw in woct:
                    dur_tot += iw.duration
                context['wts'][wt].append(('Total Duration', dur_tot))
            if wt.has_distance_comp:
                for iw in woct:
                    dist_tot += iw.dist
                context['wts'][wt].append(('Total Distance', dist_tot))
            if dur_tot != 0 and dist_tot != 0:
                m26d = m26.Distance(dist_tot.mi)
                m26t = m26.ElapsedTime(int(dur_tot.total_seconds()))
                m26s = m26.Speed(m26d, m26t)
                try:
                    context['wts'][wt].append(('Pace per Mile', m26s.pace_per_mile()))
                except:
                    pass # divide by zero for Pace per mile
            if wt.has_first_count_component:
                fcc_tot = 0
                for iw in woct:
                    fcc_tot += iw.raw_count
                context['wts'][wt].append(('Total ' + wt.first_count_component.type_name, fcc_tot))
            if wt.has_second_count_component:
                scc_tot = 0
                for iw in woct:
                    scc_tot += iw.second_raw_count
                context['wts'][wt].append(('Total ' + wt.second_count_component.type_name, scc_tot))
            if wt.has_weight_comp:
                for iw in woct:
                    weight_tot += iw.weight
                context['wts'][wt].append(('Average Weight per Workout', weight_tot / len(woct)))
            if wt.has_set_rep_comp:
                st = 0
                rt = 0
                for iw in woct:
                    st += iw.raw_set
                    rt += (iw.raw_set * iw.raw_rep)
                avg_rps = rt / st
                context['wts'][wt].append(('Total Sets', st))
                context['wts'][wt].append(('Average Reps per Set', avg_rps))
                context['wts'][wt].append(('Total Reps', rt))
                if weight_tot != 0:
                    weight_tot_w = Weight()
                    for iw in woct:
                        weight_tot_w += (iw.raw_set * iw.raw_rep) * iw.weight
                    try:
                        context['wts'][wt].append(('Average Weight per Rep', weight_tot_w / rt))
                    except:
                        print("divide by zero for Average Weight per Rep")
    for ct in WorkoutTypeCount.objects.all():
        cc = 0
        for wt in WorkoutType.objects.all():
            if wt.has_first_count_component and (wt.first_count_component == ct):
                for iw in user_workouts.filter(workoutType=wt):
                    cc += iw.raw_count
            if wt.has_second_count_component and (wt.second_count_component == ct):
                for iw in user_workouts.filter(workoutType=wt):
                    cc += iw.second_raw_count
        if cc != 0:
            context['cts'][ct] = cc
    # print(context)
    # for v in context['wts']:
    #     for a in context['wts'][v]:
    #         print(a)
    return render(request, 'workout_app/workout_summary.html', context)

def newWorkoutType(request):
    if request.user.is_anonymous:
        messages.error(request, LE)
        return HttpResponseRedirect('/login/')
    if request.method == 'POST':
        form = WorkoutTypeForm(request.POST)
        if form.is_valid():
            ots = form.save(commit=False)
            ots.profile = request.user
            ots.save()
            return HttpResponseRedirect('/add_workout_linked/')
    else:
        form = WorkoutTypeForm()
    return render(request, 'workout_app/add_workout_type.html', {'form': form})

def newWorkoutLinked(request):
    if request.user.is_anonymous:
        messages.error(request, LE)
        return HttpResponseRedirect('/login/')
    if request.method == 'POST':
        form = WorkoutLinkedForm(request.POST)
        if form.is_valid():
            ots = form.save(commit=False)
            ots.profile = request.user
            ots.save()
            return HttpResponseRedirect('/workout_linked_list')
    else:
        form = WorkoutLinkedForm()
    return render(request, 'workout_app/add_workout_linked.html', {'form': form})

def newWorkoutTypeCount(request):
    if request.user.is_anonymous:
        messages.error(request,LE)
        return HttpResponseRedirect('/login/')
    if request.method == 'POST':
        form = WorkoutTypeCountForm(request.POST)
        if form.is_valid():
            ots = form.save(commit=False)
            ots.profile = request.user
            ots.save()
            return HttpResponseRedirect('/add_workout_linked/')
    else:
        form = WorkoutTypeCountForm()
    return render(request, 'workout_app/add_workout_type_count.html', {'form': form})

# def weather(request):
#     # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4b11880620bbfa64946645fe86d99eb5'
#     # city = 'Charlottesville'
#     # city_weather = requests.get(url.format(city)).json()

#     url = 'http://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=4b11880620bbfa64946645fe86d99eb5'

#     cities = City.objects.all()

#     if request.method == 'POST':
#         form = CityForm(request.POST)
#         if form not in cities:
#             form.save()

#     form = CityForm()

#     weather_stats = []

#     for city in cities:
#         city_weather = requests.get(url.format(city)).json()

#         current_weather = {
#             'city' : city_weather['name'],
#             'temperature' : city_weather['main']['temp'],
#             'description' : city_weather['weather'][0]['description'],
#             'icon' : city_weather['weather'][0]['icon']
#         }

#         weather_stats.append(current_weather)

#     context = {'weather_stats' : weather_stats, 'form' : form}

#     return render(request, 'workout_app/weather.html', context)