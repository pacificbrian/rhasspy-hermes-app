"""Example app to react to an intent to tell you the time."""
import logging
import threading,asyncio
import signal
from datetime import datetime

from rhasspyhermes.nlu import NluIntent
from rhasspyhermes_app import EndSession, HermesApp

_LOGGER = logging.getLogger("Intent2")
loop = asyncio.new_event_loop()

def start_app():
    asyncio.set_event_loop(loop)
    app = HermesApp("TimeApp", port=12183)
    loop.close()
    print("set up HermesApp {}".format(app))

    @app.on_intent("GetTime")
    async def get_time(intent: NluIntent):
        """Tell the time."""
        now = datetime.now().strftime("%H %M")
        app.notify(f"Hi, It's now {now}")
        print("got intent! => GetTime")
        return EndSession("End of session")
    return app

app = start_app()

def run_app():
    app.run()
    print("start_app end")

def cancel_all_tasks(loop):
    to_cancel = tasks.all_tasks(loop)
    if not to_cancel:
        return

    for task in to_cancel:
        task.cancel()

    loop.stop()

def cancel_app():
    print("try to terminate app.run")
    app.stop()
    None

#signal.signal(signal.SIGINT, handler)
threading.Timer(10, cancel_app).start()

t1 = threading.Thread(target=run_app, daemon=True)
t1.start()
t1.join()
