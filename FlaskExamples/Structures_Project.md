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
  - __init__.py        <br/>
  - <b>A-userManagement/</b>  <br/>
        - __init__.py  <br/>
        - views.py     <br/>
        - static/      <br/>
        - templates/   <br/>
  - <b>B-adminPanel/</b>      <br/>
        -  __init__.py  <br/>
        - views.py      <br/>
        - static/       <br/>
        - templates/    <br/>
  - <b>C-dashboard/</b>       <br/>
        - __init__.py   <br/>
        - views.py      <br/>
        - static/       <br/>
        - templates/    <br/>
 - models.py
