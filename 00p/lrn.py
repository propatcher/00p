class Daily:
    days = {"Понедельник" : "", "Вторник" : "", "Среда" : ""}
    def __init__(self, day_index=1, day_name="Monday", task="-"):
        self.day_index = day_index
        self.day_name = day_name
        self.task = task
    def add_task(self,day_name,task):
        self.task = task
        self.day_name = day_name
        self.days[f"{day_name}"] = task
        show = f"{self.day_name} : {self.task}"
    def complete_task(self,day_name):
        self.days[f"{day_name}"] = ""
    def daily_show(self):
        print(f"\n {self.days}")
    
Bob = Daily()
Bob.add_task("Понедельник", "Уроки")
Bob.daily_show()
Bob.add_task("Вторник", "Спорт")

Bob.daily_show()