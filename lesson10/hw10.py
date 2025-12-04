TASK1

from datetime import datetime


class Task:
    def __init__(self, title: str, description: str, due_date: str):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = False   # False = incomplete, True = complete

    def mark_complete(self):
        self.status = True

    def __str__(self):
        status_text = "✔ Completed" if self.status else "✘ Incomplete"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {status_text}\n"



class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def mark_task_complete(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print("Task marked as complete!")
        else:
            print("Invalid task number.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\n--- ALL TASKS ---")
        for i, task in enumerate(self.tasks):
            print(f"Task #{i}")
            print(task)

    def list_incomplete_tasks(self):
        incomplete = [t for t in self.tasks if not t.status]
        if not incomplete:
            print("No incomplete tasks.")
            return
        print("\n--- INCOMPLETE TASKS ---")
        for task in incomplete:
            print(task)



def main():
    todo = ToDoList()

    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (e.g. 2025-12-31): ")

            task = Task(title, description, due_date)
            todo.add_task(task)
            print("Task added successfully!")

        elif choice == "2":
            todo.list_all_tasks()
            index = int(input("Enter task number to mark complete: "))
            todo.mark_task_complete(index)

        elif choice == "3":
            todo.list_all_tasks()

        elif choice == "4":
            todo.list_incomplete_tasks()

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")



if __name__ == "__main__":
    main()


TASK2

from datetime import datetime


class Post:
    def __init__(self, title: str, content: str, author: str):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()

    def edit(self, new_title: str, new_content: str):
        self.title = new_title
        self.content = new_content

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Posted On: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Content:\n{self.content}\n"
            "---------------------------\n"
        )



class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post: Post):
        self.posts.append(post)
        print("Post added successfully!")

    def list_all_posts(self):
        if not self.posts:
            print("No posts found.")
            return
        print("\n--- ALL POSTS ---")
        for i, post in enumerate(self.posts):
            print(f"Post #{i}")
            print(post)

    def list_posts_by_author(self, author: str):
        filtered = [p for p in self.posts if p.author.lower() == author.lower()]
        if not filtered:
            print("No posts found for this author.")
            return
        print(f"\n--- POSTS BY {author} ---")
        for post in filtered:
            print(post)

    def delete_post(self, index: int):
        if 0 <= index < len(self.posts):
            removed = self.posts.pop(index)
            print(f"Deleted post: {removed.title}")
        else:
            print("Invalid post number.")

    def edit_post(self, index: int, new_title: str, new_content: str):
        if 0 <= index < len(self.posts):
            self.posts[index].edit(new_title, new_content)
            print("Post updated successfully!")
        else:
            print("Invalid post number.")

    def latest_posts(self, count: int = 3):
        if not self.posts:
            print("No posts found.")
            return
        latest = sorted(self.posts, key=lambda p: p.created_at, reverse=True)[:count]
        print(f"\n--- LATEST {count} POSTS ---")
        for post in latest:
            print(post)



def main():
    blog = Blog()

    while True:
        print("\n--- Simple Blog System ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. List Posts by Author")
        print("4. Delete a Post")
        print("5. Edit a Post")
        print("6. Display Latest Posts")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == "1":
            title = input("Enter title: ")
            content = input("Enter content: ")
            author = input("Enter author: ")
            post = Post(title, content, author)
            blog.add_post(post)

        elif choice == "2":
            blog.list_all_posts()

        elif choice == "3":
            author = input("Enter author name: ")
            blog.list_posts_by_author(author)

        elif choice == "4":
            blog.list_all_posts()
            index = int(input("Enter post number to delete: "))
            blog.delete_post(index)

        elif choice == "5":
            blog.list_all_posts()
            index = int(input("Enter post number to edit: "))
            new_title = input("Enter new title: ")
            new_content = input("Enter new content: ")
            blog.edit_post(index, new_title, new_content)

        elif choice == "6":
            count = int(input("How many latest posts? (default 3): ") or "3")
            blog.latest_posts(count)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")



if __name__ == "__main__":
    main()

