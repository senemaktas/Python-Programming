### Functional Structure

- spesificProject/
  - 1-__init__.py
  - 2-static/
  - 3-templates/ <br/>
        - userManagement/ <br/>
        - adminPanel/ <br/>
        - dashboard/  <br/>
  - 4-views/ <br/>
        - __init__.py <br/>
        - userManagement.py <br/>
        - adminPanel.py <br/>
        - dashboard.py <br/>
  - 5-models.py

### Split Structure

- spesificProject/
  - <b>A-__init__.py <b>   <br/>
  - <b>B-userManagement/</b>  <br/>
        - __init__.py  <br/>
        - views.py     <br/>
        - static/      <br/>
        - templates/   <br/>
  - <b>C-adminPanel/</b>  <br/>
        -  __init__.py  <br/>
        - views.py      <br/>
        - static/       <br/>
        - templates/    <br/>
  - <b>D-dashboard/</b>  <br/>
        - __init__.py   <br/>
        - views.py      <br/>
        - static/       <br/>
        - templates/    <br/>
  - <b>E-model.py/</b>  <br/>  


Some useful sources for Flask:
- https://techwithtim.net/tutorials/flask/
- http://exploreflask.com/en/latest/blueprints.html
