class Task {
    constructor(id, title, description, priority) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.priority = priority;
        this.completed = false;
    }

    markComplete() {
        this.completed = true;
    }

    updateTitle(newTitle) {
        this.title = newTitle;
    }
}

class TaskManager {
    constructor() {
        this.tasks = [];
    }

    addTask(task) {
        this.tasks.push(task);
    }

    getTaskById(id) {
        return this.tasks.find(task => task.id === id);
    }

    deleteTask(id) {
        this.tasks = this.tasks.filter(task => task.id !== id);
    }

    getPendingTasks() {
        return this.tasks.filter(task => !task.completed);
    }
}

// Example Usage
const taskManager = new TaskManager();
const task1 = new Task(1, "Learn JavaScript", "Complete the JS tutorials", "high");
taskManager.addTask(task1);

const task2 = new Task(2, "Buy Groceries", "Purchase items for the week", "medium");
taskManager.addTask(task2);

task1.markComplete();  // Mark the task as completed
