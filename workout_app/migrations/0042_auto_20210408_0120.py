# Generated by Django 3.1.7 on 2021-04-08 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_app', '0041_auto_20210407_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='icon',
            field=models.CharField(choices=[('award-badge-star-1.png', 'award-badge-star-1.png'), ('landmarks-stone.png', 'landmarks-stone.png'), ('outdoors-bird.png', 'outdoors-bird.png'), ('shooting-rifle-aim.png', 'shooting-rifle-aim.png'), ('love-it-warning.png', 'love-it-warning.png'), ('canoe-2.png', 'canoe-2.png'), ('fitness-shaker.png', 'fitness-shaker.png'), ('fishing-hook-fish.png', 'fishing-hook-fish.png'), ('soccer-kick-ball.png', 'soccer-kick-ball.png'), ('ping-pong-paddle.png', 'ping-pong-paddle.png'), ('award-medal-shine.png', 'award-medal-shine.png'), ('trends-hot.png', 'trends-hot.png'), ('sport-paragliding.png', 'sport-paragliding.png'), ('skateboard-1.png', 'skateboard-1.png'), ('social-profile-avatar.png', 'social-profile-avatar.png'), ('pool-player.png', 'pool-player.png'), ('landmarks-monument.png', 'landmarks-monument.png'), ('yoga-arm-stretch.png', 'yoga-arm-stretch.png'), ('gymnastics-ribbon-person.png', 'gymnastics-ribbon-person.png'), ('mood-happy-laptop.png', 'mood-happy-laptop.png'), ('swimming-cap.png', 'swimming-cap.png'), ('paralympics-archery.png', 'paralympics-archery.png'), ('canoe-3.png', 'canoe-3.png'), ('fitness-six-pack.png', 'fitness-six-pack.png'), ('like-ribbon.png', 'like-ribbon.png'), ('paralympics-javelin-throwing.png', 'paralympics-javelin-throwing.png'), ('skateboard-person.png', 'skateboard-person.png'), ('baseball-glove.png', 'baseball-glove.png'), ('baseball-score.png', 'baseball-score.png'), ('golf-equipment.png', 'golf-equipment.png'), ('badminton-shuttlecock.png', 'badminton-shuttlecock.png'), ('canoe-person-1.png', 'canoe-person-1.png'), ('martial-arts-helmet.png', 'martial-arts-helmet.png'), ('boxing-bag-small.png', 'boxing-bag-small.png'), ('love-it-settings.png', 'love-it-settings.png'), ('paralympics-tennis.png', 'paralympics-tennis.png'), ('beach-parasol-water-1.png', 'beach-parasol-water-1.png'), ('skiing-skiis.png', 'skiing-skiis.png'), ('canoe-1.png', 'canoe-1.png'), ('volleyball-ball.png', 'volleyball-ball.png'), ('diving-diver.png', 'diving-diver.png'), ('award-trophy-star-1.png', 'award-trophy-star-1.png'), ('flag.png', 'flag.png'), ('beach-palm-sunbed.png', 'beach-palm-sunbed.png'), ('love-it-download.png', 'love-it-download.png'), ('outdoors-fire-camp.png', 'outdoors-fire-camp.png'), ('beach-person-water-parasol.png', 'beach-person-water-parasol.png'), ('camping-tent-person.png', 'camping-tent-person.png'), ('love-it-lock.png', 'love-it-lock.png'), ('gymnastics-acrobatic-1.png', 'gymnastics-acrobatic-1.png'), ('mood-rock.png', 'mood-rock.png'), ('fitness-biceps.png', 'fitness-biceps.png'), ('outdoors-barn-bench.png', 'outdoors-barn-bench.png'), ('like-shine.png', 'like-shine.png'), ('golf-hole-aim.png', 'golf-hole-aim.png'), ('yoga-cobra.png', 'yoga-cobra.png'), ('like-plus-one.png', 'like-plus-one.png'), ('award-badge.png', 'award-badge.png'), ('gift-box-1.png', 'gift-box-1.png'), ('gift-electronic.png', 'gift-electronic.png'), ('love-it-add.png', 'love-it-add.png'), ('award-trophy-person.png', 'award-trophy-person.png'), ('gaming-ribbon-100.png', 'gaming-ribbon-100.png'), ('certified-diploma-1.png', 'certified-diploma-1.png'), ('soccer-player-kick.png', 'soccer-player-kick.png'), ('paralympics-racing.png', 'paralympics-racing.png'), ('award-ribbon-star.png', 'award-ribbon-star.png'), ('camping-tent-forest.png', 'camping-tent-forest.png'), ('skating.png', 'skating.png'), ('camping-shelter.png', 'camping-shelter.png'), ('fitness-dumbbell-disk-weight.png', 'fitness-dumbbell-disk-weight.png'), ('flag-question.png', 'flag-question.png'), ('outdoors-woodchopping.png', 'outdoors-woodchopping.png'), ('gaming-10.png', 'gaming-10.png'), ('gaming-trophy-10.png', 'gaming-trophy-10.png'), ('rating-star-square.png', 'rating-star-square.png'), ('bowling-pins.png', 'bowling-pins.png'), ('outdoors-kite-flying-cloud.png', 'outdoors-kite-flying-cloud.png'), ('diving-boat.png', 'diving-boat.png'), ('athletics-shooting.png', 'athletics-shooting.png'), ('volleyball-net.png', 'volleyball-net.png'), ('boxing-bag-hanging.png', 'boxing-bag-hanging.png'), ('fitness-dumbells-sizes.png', 'fitness-dumbells-sizes.png'), ('badminton-shuttlecock-racquet.png', 'badminton-shuttlecock-racquet.png'), ('climbing-mountain.png', 'climbing-mountain.png'), ('dislike.png', 'dislike.png'), ('bowling-set.png', 'bowling-set.png'), ('love-it-flag.png', 'love-it-flag.png'), ('canoe-person.png', 'canoe-person.png'), ('martial-arts-fencing-person.png', 'martial-arts-fencing-person.png'), ('outdoors-camp-fire.png', 'outdoors-camp-fire.png'), ('ski-jumping.png', 'ski-jumping.png'), ('outdoors-camp-fire-guitar.png', 'outdoors-camp-fire-guitar.png'), ('fitness-protein.png', 'fitness-protein.png'), ('skiing-bobsled.png', 'skiing-bobsled.png'), ('golf-hole.png', 'golf-hole.png'), ('flag-triangle-1.png', 'flag-triangle-1.png'), ('love-it-break.png', 'love-it-break.png'), ('rating-star-add.png', 'rating-star-add.png'), ('gaming-ribbon-10.png', 'gaming-ribbon-10.png'), ('trekking-person.png', 'trekking-person.png'), ('outdoors-bubble-ball.png', 'outdoors-bubble-ball.png'), ('outdoors-kite-flying.png', 'outdoors-kite-flying.png'), ('yoga-stretch.png', 'yoga-stretch.png'), ('camping-rv.png', 'camping-rv.png'), ('flag-settings.png', 'flag-settings.png'), ('outdoors-nps.png', 'outdoors-nps.png'), ('outdoors-camp-flame.png', 'outdoors-camp-flame.png'), ('pool-ball.png', 'pool-ball.png'), ('gymnastics-rhythmic-ribbon.png', 'gymnastics-rhythmic-ribbon.png'), ('love-it-disable.png', 'love-it-disable.png'), ('fitness-grip-weights.png', 'fitness-grip-weights.png'), ('fitness-bicycle-1.png', 'fitness-bicycle-1.png'), ('flag-plain-3.png', 'flag-plain-3.png'), ('gymnastics-acrobatic.png', 'gymnastics-acrobatic.png'), ('love-it.png', 'love-it.png'), ('camping-tent.png', 'camping-tent.png'), ('yoga-back-stretch.png', 'yoga-back-stretch.png'), ('fitness-jumping-rope-1.png', 'fitness-jumping-rope-1.png'), ('dislike-1.png', 'dislike-1.png'), ('landmarks-statue-flag.png', 'landmarks-statue-flag.png'), ('sailing-boat-water-1.png', 'sailing-boat-water-1.png'), ('golf-ball.png', 'golf-ball.png'), ('martial-arts-kimono.png', 'martial-arts-kimono.png'), ('mood-lock-head.png', 'mood-lock-head.png'), ('love-it-upload.png', 'love-it-upload.png'), ('martial-arts-sword-fencing-1.png', 'martial-arts-sword-fencing-1.png'), ('outdoors-woodchopping-1.png', 'outdoors-woodchopping-1.png'), ('nautic-sports-surfing-water.png', 'nautic-sports-surfing-water.png'), ('vip-crown-king.png', 'vip-crown-king.png'), ('sailing-archor.png', 'sailing-archor.png'), ('tennis-racquet.png', 'tennis-racquet.png'), ('fitness-machine.png', 'fitness-machine.png'), ('gymnastics-ribbon-person-2.png', 'gymnastics-ribbon-person-2.png'), ('love-it-share.png', 'love-it-share.png'), ('outdoors-camp-fire-make.png', 'outdoors-camp-fire-make.png'), ('yoga-bridge.png', 'yoga-bridge.png'), ('camping-tent-sleep.png', 'camping-tent-sleep.png'), ('paralympics-discus-throwing.png', 'paralympics-discus-throwing.png'), ('boxing-boxer.png', 'boxing-boxer.png'), ('flag-1.png', 'flag-1.png'), ('beach-palm.png', 'beach-palm.png'), ('love-it-phone.png', 'love-it-phone.png'), ('gaming-second-place.png', 'gaming-second-place.png'), ('paralympics-running.png', 'paralympics-running.png'), ('flag-check.png', 'flag-check.png'), ('golf-cart.png', 'golf-cart.png'), ('shooting-rifle.png', 'shooting-rifle.png'), ('flag-plain-2.png', 'flag-plain-2.png'), ('sailing-boat.png', 'sailing-boat.png'), ('dancing-ballet-dress.png', 'dancing-ballet-dress.png'), ('fitness-bicycle-2.png', 'fitness-bicycle-2.png'), ('swimming-diving.png', 'swimming-diving.png'), ('climbing-sports.png', 'climbing-sports.png'), ('fitness-jumping-rope-2.png', 'fitness-jumping-rope-2.png'), ('sport-curling-1.png', 'sport-curling-1.png'), ('yoga-stretch-1.png', 'yoga-stretch-1.png'), ('dislike-2.png', 'dislike-2.png'), ('like-chat.png', 'like-chat.png'), ('award-trophy-1.png', 'award-trophy-1.png'), ('award-medal-4.png', 'award-medal-4.png'), ('archery-person.png', 'archery-person.png'), ('american-football-run-ball-1.png', 'american-football-run-ball-1.png'), ('fitness-slim-waist.png', 'fitness-slim-waist.png'), ('gymnastics-ribbon-person-1.png', 'gymnastics-ribbon-person-1.png'), ('mood-question.png', 'mood-question.png'), ('outdoors-horse.png', 'outdoors-horse.png'), ('mood-happy.png', 'mood-happy.png'), ('swimming-goggles.png', 'swimming-goggles.png'), ('gaming-ribbon-first.png', 'gaming-ribbon-first.png'), ('rating-star-badge.png', 'rating-star-badge.png'), ('social-profile-network.png', 'social-profile-network.png'), ('skiing-snow-scooter.png', 'skiing-snow-scooter.png'), ('nautic-sports-scooter-1.png', 'nautic-sports-scooter-1.png'), ('outdoors-dog-house.png', 'outdoors-dog-house.png'), ('fishing-lure.png', 'fishing-lure.png'), ('american-football-goal.png', 'american-football-goal.png'), ('rating-star-ribbon.png', 'rating-star-ribbon.png'), ('love-it-ribbon.png', 'love-it-ribbon.png'), ('social-profile-click.png', 'social-profile-click.png'), ('fitness-weights.png', 'fitness-weights.png'), ('love-it-hand-give.png', 'love-it-hand-give.png'), ('fitness-jumping-rope-3.png', 'fitness-jumping-rope-3.png'), ('nautic-sports-sailing.png', 'nautic-sports-sailing.png'), ('flag-skull.png', 'flag-skull.png'), ('flag-plain-1.png', 'flag-plain-1.png'), ('flag-flash.png', 'flag-flash.png'), ('ranking-ribbon-1.png', 'ranking-ribbon-1.png'), ('volleyball-smash.png', 'volleyball-smash.png'), ('fitness-bicycle-3.png', 'fitness-bicycle-3.png'), ('paralympics-torch.png', 'paralympics-torch.png'), ('yoga-full-body-stretch.png', 'yoga-full-body-stretch.png'), ('rollerblades-person.png', 'rollerblades-person.png'), ('soccer-goal-net.png', 'soccer-goal-net.png'), ('skateboard-person-1.png', 'skateboard-person-1.png'), ('vip-crown-queen-2.png', 'vip-crown-queen-2.png'), ('yoga-mat.png', 'yoga-mat.png'), ('award-medal.png', 'award-medal.png'), ('paralympics-fencing.png', 'paralympics-fencing.png'), ('award-star.png', 'award-star.png'), ('like-dislike.png', 'like-dislike.png'), ('american-football-ball.png', 'american-football-ball.png'), ('outdoors-water-flask.png', 'outdoors-water-flask.png'), ('award-medal-1.png', 'award-medal-1.png'), ('basketball-ball.png', 'basketball-ball.png'), ('archery-bow-1.png', 'archery-bow-1.png'), ('athletics-javelin-throwing.png', 'athletics-javelin-throwing.png'), ('outdoors-barbeque.png', 'outdoors-barbeque.png'), ('sport-horse-riding.png', 'sport-horse-riding.png'), ('outdoors-camp-fire-marshmallows.png', 'outdoors-camp-fire-marshmallows.png'), ('athletics-jumping.png', 'athletics-jumping.png'), ('rating-half-star.png', 'rating-half-star.png'), ('american-football-helmet.png', 'american-football-helmet.png'), ('biking-person.png', 'biking-person.png'), ('flag-information.png', 'flag-information.png'), ('yoga-down-stretch.png', 'yoga-down-stretch.png'), ('canoe-paddles.png', 'canoe-paddles.png'), ('flag-triangle.png', 'flag-triangle.png'), ('ranking-first.png', 'ranking-first.png'), ('trekking-goal.png', 'trekking-goal.png'), ('gymnastics-acrobatic-hanging-person.png', 'gymnastics-acrobatic-hanging-person.png'), ('nautic-sports-sailing-person.png', 'nautic-sports-sailing-person.png'), ('american-football-score.png', 'american-football-score.png'), ('vip-crown-queen-1.png', 'vip-crown-queen-1.png'), ('trends-torch.png', 'trends-torch.png'), ('biking-mountain.png', 'biking-mountain.png'), ('like-click.png', 'like-click.png'), ('athletics-running.png', 'athletics-running.png'), ('martial-arts-karate.png', 'martial-arts-karate.png'), ('tennis-player.png', 'tennis-player.png'), ('rating-star-remove.png', 'rating-star-remove.png'), ('award-medal-2.png', 'award-medal-2.png'), ('gaming-trophy-5.png', 'gaming-trophy-5.png'), ('love-it-remove.png', 'love-it-remove.png'), ('tennis-ball.png', 'tennis-ball.png'), ('golf-hole-1.png', 'golf-hole-1.png'), ('rollerblades.png', 'rollerblades.png'), ('like.png', 'like.png'), ('tennis-net.png', 'tennis-net.png'), ('trends-hot-flame.png', 'trends-hot-flame.png'), ('mood-happy-smartphone.png', 'mood-happy-smartphone.png'), ('ranking-winner-ribbon.png', 'ranking-winner-ribbon.png'), ('ranking-ribbon.png', 'ranking-ribbon.png'), ('athletics-jumping-person.png', 'athletics-jumping-person.png'), ('skiing-slide-down.png', 'skiing-slide-down.png'), ('athletics-pole-vault.png', 'athletics-pole-vault.png'), ('skating-1.png', 'skating-1.png'), ('flag-warning.png', 'flag-warning.png'), ('certified-ribbon.png', 'certified-ribbon.png'), ('gaming-5.png', 'gaming-5.png'), ('ranking-star-top.png', 'ranking-star-top.png'), ('sailing-boat-2.png', 'sailing-boat-2.png'), ('skiing-chest-slide.png', 'skiing-chest-slide.png'), ('american-football-ball-1.png', 'american-football-ball-1.png'), ('yoga-meditate-1.png', 'yoga-meditate-1.png'), ('award-wall-star.png', 'award-wall-star.png'), ('outdoors-rope.png', 'outdoors-rope.png'), ('fishing-bait-fish.png', 'fishing-bait-fish.png'), ('vip-crown-queen.png', 'vip-crown-queen.png'), ('beach-palm-water.png', 'beach-palm-water.png'), ('mood-skull-chat.png', 'mood-skull-chat.png'), ('croquet-ball-hoop.png', 'croquet-ball-hoop.png'), ('camping-tent-small.png', 'camping-tent-small.png'), ('gift-heart.png', 'gift-heart.png'), ('nautic-sports-water-skiing.png', 'nautic-sports-water-skiing.png'), ('award-oscar.png', 'award-oscar.png'), ('biking-helmet-person.png', 'biking-helmet-person.png'), ('baseball-helmet.png', 'baseball-helmet.png'), ('canoe.png', 'canoe.png'), ('skiing-cross-country-1.png', 'skiing-cross-country-1.png'), ('yoga-arms-stretch.png', 'yoga-arms-stretch.png'), ('trends-torch-1.png', 'trends-torch-1.png'), ('gaming-100.png', 'gaming-100.png'), ('outdoors-camp-fire-roasting.png', 'outdoors-camp-fire-roasting.png'), ('outdoors-backpack.png', 'outdoors-backpack.png'), ('sailing-boat-3.png', 'sailing-boat-3.png'), ('swimming-diving-board.png', 'swimming-diving-board.png'), ('soccer-player.png', 'soccer-player.png'), ('olympics-torch.png', 'olympics-torch.png'), ('skiing-cross-country.png', 'skiing-cross-country.png'), ('trekking-shelter.png', 'trekking-shelter.png'), ('skating-shoes.png', 'skating-shoes.png'), ('fitness-bicycle.png', 'fitness-bicycle.png'), ('canoe-single.png', 'canoe-single.png'), ('sailing-boat-1.png', 'sailing-boat-1.png'), ('award-star-head.png', 'award-star-head.png'), ('fishing-line.png', 'fishing-line.png'), ('love-it-bubble.png', 'love-it-bubble.png'), ('beach-palm-water-1.png', 'beach-palm-water-1.png'), ('martial-arts-sword-fencing.png', 'martial-arts-sword-fencing.png'), ('rating-star-bubble.png', 'rating-star-bubble.png'), ('love-it-sync.png', 'love-it-sync.png'), ('paralympics-flag.png', 'paralympics-flag.png'), ('social-profile-smartphone-add.png', 'social-profile-smartphone-add.png'), ('mood-moody.png', 'mood-moody.png'), ('fitness-hand-grip.png', 'fitness-hand-grip.png'), ('archery-bow.png', 'archery-bow.png'), ('swimming-cap-1.png', 'swimming-cap-1.png'), ('canoe-paddles-1.png', 'canoe-paddles-1.png'), ('outdoors-shelter-home.png', 'outdoors-shelter-home.png'), ('rating-star-three.png', 'rating-star-three.png'), ('rating-star.png', 'rating-star.png'), ('love-it-angel.png', 'love-it-angel.png'), ('award-star-1.png', 'award-star-1.png'), ('fishing-fail.png', 'fishing-fail.png'), ('trekking-mountain.png', 'trekking-mountain.png'), ('fitness-weighlifting-bench.png', 'fitness-weighlifting-bench.png'), ('yoga-shoulder-stretch.png', 'yoga-shoulder-stretch.png'), ('yoga-meditate.png', 'yoga-meditate.png'), ('nautic-sports-surfing.png', 'nautic-sports-surfing.png'), ('gymnastics-acrobatic-hanging.png', 'gymnastics-acrobatic-hanging.png'), ('pool-triangle.png', 'pool-triangle.png'), ('martial-arts-sumo.png', 'martial-arts-sumo.png'), ('trekking-stick.png', 'trekking-stick.png'), ('love-it-search.png', 'love-it-search.png'), ('shooting-rifle-person-aim.png', 'shooting-rifle-person-aim.png'), ('outdoors-pig-apple.png', 'outdoors-pig-apple.png'), ('soccer-field.png', 'soccer-field.png'), ('outdoors-swiss-knife.png', 'outdoors-swiss-knife.png'), ('sailing-finish-line.png', 'sailing-finish-line.png'), ('diving-oxygen.png', 'diving-oxygen.png'), ('award-badge-star.png', 'award-badge-star.png'), ('hockey-puck-stick.png', 'hockey-puck-stick.png'), ('fitness-pilates-ball.png', 'fitness-pilates-ball.png'), ('skiing-board-slide.png', 'skiing-board-slide.png'), ('trends-hot-1.png', 'trends-hot-1.png'), ('camping-sleeping-bag.png', 'camping-sleeping-bag.png'), ('nautic-sports-scooter.png', 'nautic-sports-scooter.png'), ('paralympics-ball.png', 'paralympics-ball.png'), ('ranking-people-first.png', 'ranking-people-first.png'), ('rating-star-subtract.png', 'rating-star-subtract.png'), ('badminton-player.png', 'badminton-player.png'), ('vip-royal.png', 'vip-royal.png'), ('skiing-cable-car.png', 'skiing-cable-car.png'), ('gaming-treasure-add.png', 'gaming-treasure-add.png'), ('diving-fins.png', 'diving-fins.png'), ('swimming-waterpolo.png', 'swimming-waterpolo.png'), ('fishing-fish.png', 'fishing-fish.png'), ('martial-arts-mask-helmet.png', 'martial-arts-mask-helmet.png'), ('trends-hashtag.png', 'trends-hashtag.png'), ('mood-peace.png', 'mood-peace.png'), ('gift-circle.png', 'gift-circle.png'), ('outdoors-backpack-1.png', 'outdoors-backpack-1.png'), ('biking-helmet.png', 'biking-helmet.png'), ('rating-star-top.png', 'rating-star-top.png'), ('soccer-goalkeeper-glove-1.png', 'soccer-goalkeeper-glove-1.png'), ('rating-star-circle.png', 'rating-star-circle.png'), ('fitness-heart-rate.png', 'fitness-heart-rate.png'), ('ping-pong-player.png', 'ping-pong-player.png'), ('love-it-circle.png', 'love-it-circle.png'), ('outdoors-bird-house.png', 'outdoors-bird-house.png'), ('outdoors-bird-house-1.png', 'outdoors-bird-house-1.png'), ('gymnastics-rhythmic-ribbon-1.png', 'gymnastics-rhythmic-ribbon-1.png'), ('rating-star-check.png', 'rating-star-check.png'), ('fishing-catch.png', 'fishing-catch.png'), ('outdoors-bench-sit.png', 'outdoors-bench-sit.png'), ('boxing-glove.png', 'boxing-glove.png'), ('gymnastics-weightlifting.png', 'gymnastics-weightlifting.png'), ('pool-table.png', 'pool-table.png'), ('like-plus.png', 'like-plus.png'), ('certified-ribbon-1.png', 'certified-ribbon-1.png'), ('landmarks-view-point.png', 'landmarks-view-point.png'), ('flag-plain.png', 'flag-plain.png'), ('rating-star-1.png', 'rating-star-1.png'), ('vip.png', 'vip.png'), ('gymnastics-jump.png', 'gymnastics-jump.png'), ('love-it-subtract.png', 'love-it-subtract.png'), ('camping-tent-2.png', 'camping-tent-2.png'), ('mood-warning.png', 'mood-warning.png'), ('sport-curling.png', 'sport-curling.png'), ('gymnastics-acrobatic-hanging-1.png', 'gymnastics-acrobatic-hanging-1.png'), ('ranking-stars-ribbon.png', 'ranking-stars-ribbon.png'), ('fitness-weightlift.png', 'fitness-weightlift.png'), ('certified-certificate.png', 'certified-certificate.png'), ('beach-sun-birds.png', 'beach-sun-birds.png'), ('swimming-lifeguard.png', 'swimming-lifeguard.png'), ('camping-tent-3.png', 'camping-tent-3.png'), ('social-profile-bubble.png', 'social-profile-bubble.png'), ('ranking-winner.png', 'ranking-winner.png'), ('outdoors-shelter.png', 'outdoors-shelter.png'), ('skateboard.png', 'skateboard.png'), ('yoga-back-stretch-1.png', 'yoga-back-stretch-1.png'), ('baseball-player.png', 'baseball-player.png'), ('outdoors-rope-1.png', 'outdoors-rope-1.png'), ('certified-diploma.png', 'certified-diploma.png'), ('shooting-target.png', 'shooting-target.png'), ('tennis-forehand.png', 'tennis-forehand.png'), ('cricket-bat-ball .png', 'cricket-bat-ball .png'), ('beach-sunbed.png', 'beach-sunbed.png'), ('like-ribbon-1.png', 'like-ribbon-1.png'), ('vip-crown.png', 'vip-crown.png'), ('like-bubble.png', 'like-bubble.png'), ('sport-hockey.png', 'sport-hockey.png'), ('soccer-player-ball.png', 'soccer-player-ball.png'), ('athletics-long-jumping.png', 'athletics-long-jumping.png'), ('certified-ribbon-2.png', 'certified-ribbon-2.png'), ('sailing-boat-water.png', 'sailing-boat-water.png'), ('diving-mask-fish.png', 'diving-mask-fish.png'), ('camping-tent-map.png', 'camping-tent-map.png'), ('athletics-discus-throwing.png', 'athletics-discus-throwing.png'), ('martial-arts-fencing.png', 'martial-arts-fencing.png'), ('outdoors-mining.png', 'outdoors-mining.png'), ('ranking-winner-medal.png', 'ranking-winner-medal.png'), ('rating-star-give-1.png', 'rating-star-give-1.png'), ('climbing-head-light.png', 'climbing-head-light.png'), ('outdoors-machete.png', 'outdoors-machete.png'), ('camping-tent-1.png', 'camping-tent-1.png'), ('golf-player.png', 'golf-player.png'), ('skiing-snow-scooter-person.png', 'skiing-snow-scooter-person.png'), ('gaming-first-place.png', 'gaming-first-place.png'), ('love-it-text.png', 'love-it-text.png'), ('gymnastics-acrobatic-hanging-2.png', 'gymnastics-acrobatic-hanging-2.png'), ('sailing-boat-person.png', 'sailing-boat-person.png'), ('paralympics-football.png', 'paralympics-football.png'), ('diving-mask.png', 'diving-mask.png'), ('fitness-dumbbell-lift.png', 'fitness-dumbbell-lift.png'), ('flags.png', 'flags.png'), ('golf-hole-ball.png', 'golf-hole-ball.png'), ('gift-box.png', 'gift-box.png'), ('vip-circle.png', 'vip-circle.png'), ('skiing-cable-car-1.png', 'skiing-cable-car-1.png'), ('trekking-map.png', 'trekking-map.png'), ('fishing-hook-fish-1.png', 'fishing-hook-fish-1.png'), ('yoga-back-stretch-2.png', 'yoga-back-stretch-2.png'), ('boxing-boxer-bag.png', 'boxing-boxer-bag.png'), ('outdoors-flashlight.png', 'outdoors-flashlight.png'), ('athletics-team-running.png', 'athletics-team-running.png'), ('like-plus-bubble.png', 'like-plus-bubble.png'), ('baseball-bat-ball.png', 'baseball-bat-ball.png'), ('fitness-jumping-rope.png', 'fitness-jumping-rope.png'), ('diving-oxygen-tank.png', 'diving-oxygen-tank.png'), ('biking-learner.png', 'biking-learner.png'), ('landmarks-telescope-person.png', 'landmarks-telescope-person.png'), ('like-1.png', 'like-1.png'), ('love-it-ribbon-2.png', 'love-it-ribbon-2.png'), ('award-badge-1.png', 'award-badge-1.png'), ('skiing-ice-skates.png', 'skiing-ice-skates.png'), ('outdoors-flame-lantern.png', 'outdoors-flame-lantern.png'), ('martial-arts-swords.png', 'martial-arts-swords.png'), ('award-ribbon-star-2.png', 'award-ribbon-star-2.png'), ('bowling-player.png', 'bowling-player.png'), ('outdoors-flashlight-2.png', 'outdoors-flashlight-2.png'), ('award-ribbon-star-3.png', 'award-ribbon-star-3.png'), ('boxing-head-guard.png', 'boxing-head-guard.png'), ('gaming-treasure-find.png', 'gaming-treasure-find.png'), ('soccer-ball.png', 'soccer-ball.png'), ('skiing-snowboard.png', 'skiing-snowboard.png'), ('flag-cash.png', 'flag-cash.png'), ('athletics-running-1.png', 'athletics-running-1.png'), ('paralympics-race.png', 'paralympics-race.png'), ('rating-star-winner.png', 'rating-star-winner.png'), ('pool-black-ball.png', 'pool-black-ball.png'), ('vip-crown-king-1.png', 'vip-crown-king-1.png'), ('basketball-ball-dribble-player.png', 'basketball-ball-dribble-player.png'), ('like-circle.png', 'like-circle.png'), ('love-it-edit.png', 'love-it-edit.png'), ('shooting-rifle-target.png', 'shooting-rifle-target.png'), ('beach-swim.png', 'beach-swim.png'), ('rating-star-bubble-1.png', 'rating-star-bubble-1.png'), ('award-trophy.png', 'award-trophy.png'), ('love-it-star.png', 'love-it-star.png'), ('yoga-leg-grab-stretch.png', 'yoga-leg-grab-stretch.png'), ('flag-star.png', 'flag-star.png'), ('like-2.png', 'like-2.png'), ('love-it-ribbon-1.png', 'love-it-ribbon-1.png'), ('gaming-trophy-100.png', 'gaming-trophy-100.png'), ('award-badge-2.png', 'award-badge-2.png'), ('award-trophy-star.png', 'award-trophy-star.png'), ('helmet-sports.png', 'helmet-sports.png'), ('gymnastics-horse.png', 'gymnastics-horse.png'), ('paralympics-race-1.png', 'paralympics-race-1.png'), ('basketball-hoop.png', 'basketball-hoop.png'), ('dancing-ballet.png', 'dancing-ballet.png'), ('tennis-backhand.png', 'tennis-backhand.png'), ('award-ribbon-star-1.png', 'award-ribbon-star-1.png'), ('gaming-trophy-check.png', 'gaming-trophy-check.png'), ('pool-player-table.png', 'pool-player-table.png'), ('american-football-run-ball.png', 'american-football-run-ball.png'), ('outdoors-flashlight-1.png', 'outdoors-flashlight-1.png'), ('paralympics-swimming.png', 'paralympics-swimming.png'), ('diving-gun.png', 'diving-gun.png'), ('beach-parasol-water.png', 'beach-parasol-water.png'), ('award-badge-3.png', 'award-badge-3.png'), ('ping-pong-table.png', 'ping-pong-table.png'), ('love-it-check.png', 'love-it-check.png'), ('fitness-dumbbell.png', 'fitness-dumbbell.png'), ('rating-star-give.png', 'rating-star-give.png'), ('boxing-bag.png', 'boxing-bag.png'), ('swimming-jump.png', 'swimming-jump.png'), ('gymnastics-trampoline.png', 'gymnastics-trampoline.png'), ('paralympics-weightlifting.png', 'paralympics-weightlifting.png')], max_length=100),
        ),
    ]
