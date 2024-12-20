import asyncio
import datetime


def dest_time_with_preemption(dest_time, preemption):
    if preemption > 0:
        return dest_time - datetime.timedelta(seconds=preemption)
    else:
        return dest_time + datetime.timedelta(seconds=preemption * -1)


def delta_seconds(time1, time2):
    if time1 > time2:
        delta = (time1 - time2).total_seconds()
    else:
        delta = (time2 - time1).total_seconds() * -1
    return delta


async def wait_dest_time(dest_time: datetime.datetime):
    while True:
        current_time = datetime.datetime.now(datetime.timezone.utc)
        delta = (dest_time - current_time).total_seconds() / 2
        if delta > 20:
            await asyncio.sleep(delta)
            continue
        break

    while datetime.datetime.now(datetime.timezone.utc) <= dest_time:
        await asyncio.sleep(0.001)
