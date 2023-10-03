from aiohttp import web
from datetime import datetime
import json

class ScheduleManager:
    def __init__(self, schedule_file):
        self.schedule_file = schedule_file
        self.schedule = {}
        self.load_from_file()

    def save_to_file(self):
        with open(self.schedule_file, 'w') as f:
            json.dump(self.schedule, f)

    def load_from_file(self):
        try:
            with open(self.schedule_file, 'r') as f:
                self.schedule = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # File might not exist the first time or might be corrupt
            self.schedule = {}

    def update_schedule(self, data):
        self.schedule = data
        self.save_to_file()
        print("Schedule saved!")

    def check_run(self):
        now = datetime.now()
        weekday = now.weekday()
        hour = now.hour
        minute_block = now.minute // 15

        if str(weekday) in self.schedule and [hour, minute_block] in self.schedule[str(weekday)]:
            print("Equipment can run now!")
            return {'run': True}
        else:
            print("Equipment should not run now.")
            return {'run': False}

    def get_schedule(self):
        return self.schedule

async def handle_update_schedule(request):
    try:
        data = await request.json()
        schedule_manager.update_schedule(data)
        return web.Response(status=200, text="Schedule saved!")
    except Exception as e:
        return web.Response(status=500, text=str(e))

async def index(request):
    with open('templates/index.html', 'r') as f:
        return web.Response(text=f.read(), content_type='text/html')

async def check_run(request):
    result = schedule_manager.check_run()
    return web.json_response(result)

async def get_schedule(request):
    schedule = schedule_manager.get_schedule()
    return web.json_response(schedule)

if __name__ == "__main__":
    SCHEDULE_FILE = "schedule.json"
    schedule_manager = ScheduleManager(SCHEDULE_FILE)

    app = web.Application()
    app.router.add_get('/', index)
    app.router.add_post('/update_schedule', handle_update_schedule)
    app.router.add_get('/check_run', check_run)
    app.router.add_get('/get_schedule', get_schedule)

    # Configure static file routes for CSS and JS files
    app.router.add_static('/static/', path='static')

    web.run_app(app)
