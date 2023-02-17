from rocketry import Rocketry
from rocketry.conds import daily

app = Rocketry()

# Create some tasks:

@app.task(daily.after("15:30"))
def do_things():
    print("hello world")