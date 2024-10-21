#Blueprint for the main routes
from flask import Blueprint, render_template, request, redirect, url_for
from Models.models import Project, Task, db

main_bp = Blueprint('main_controller', __name__)

@main_bp.route('/projects')
def projects_func():
    all_projects = Project.query.all()
    return render_template('projects.html', projects=all_projects)

@main_bp.route('/projects/<int:project_id>/tasks')
def tasks_func(project_id):
    project = Project.query.get_or_404(project_id)
    tasks = Task.query.filter_by(project_id=project.id).all()
    return render_template('tasks.html', project=project, tasks=tasks)

@main_bp.route('/projects/add', methods=['GET', 'POST'])
def add_project_func():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form.get('description')
        new_project = Project(name=name, description=description)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('main_controller.projects_func'))
    return render_template('add_project.html')

@main_bp.route('/projects/<int:project_id>/tasks/add', methods=['GET', 'POST'])
def add_task_func(project_id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form.get('description')
        new_task = Task(title=title, description=description, project_id=project_id)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('main_controller.tasks_func', project_id=project_id))
    return render_template('add_task.html', project_id=project_id)

@main_bp.route('/')
def home_func():
    return render_template('home.html')

@main_bp.route('/about')
def about_func():
    return render_template('about.html')

@main_bp.route('/contact')
def contact_func():
    return render_template('contact.html')