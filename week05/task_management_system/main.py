from Services.task_service import Task_Service
from Services.user_service import User_Service




def main():
    task_service= Task_Service()
    user_Service= User_Service()

    user_Service.add_user(123, "Bonson", "bonson@gmail.com")

    task_service.create_task(1, "DSA basics", "Scratch")
    task_service.create_task(2, "DSA Advanced", "Scratch")
    task_service.create_task(3, "project", "Scratch")



    print(task_service.complete_task())
    print(task_service.complete_task())
    print(task_service.complete_task())
    print(task_service.complete_task())

    history = task_service.get_task_history()

    for i in range(history.is_empty()):
        print(history.pop().title)




if __name__ == "__main__":
    main()
