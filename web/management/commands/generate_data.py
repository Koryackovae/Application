import random
from datetime import timedelta
from random import randint

from django.core.management.base import BaseCommand
from django.utils.timezone import now

from web.models import EventSlot, User, EventSlotTag


class Command(BaseCommand):
    def handle(self, *args, **options):
        current_date = now()
        user = User.objects.first()
        tags = EventSlotTag.objects.filter(user=user)

        for day_index in range(30):
            current_date -= timedelta(days=1)

            for slot_index in range(randint(5, 10)):
                start_date = current_date + timedelta(hours=randint(0, 10))
                end_date = start_date + timedelta(hours=randint(0, 10))


                event_slot = EventSlot.objects.create(
                    title=f'generated {day_index}-{slot_index}',
                    start_date=start_date,
                    end_date=end_date,
                    is_realtime=random.choice((True, False)),
                    user=user

                )

                event_slot_tags = []
                count_of_tags = randint(0, len(tags))
                for tag_index in range(count_of_tags):
                    event_slot_tags.append(tags[tag_index])
                event_slot_tags.set(event_slot_tags)

