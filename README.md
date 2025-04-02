# NutriFitCLI (Nutirition Fitness CLI)

### Description
This is a meal and exercise tracking application that allows users to add/remove meal logs, add/remove exercise logs, view logs by date, view calories burned by day/month, and preview a monthly visual calendar for logged activities.

### Additional info:
- Developed in Python and runs from the Command Line Interface (CLI) (includig Linux/Ubuntu).
- Utilizes python modules & consists of multiple source files.
- Covers advanced features covered in ENGR 5200G including arrays, for loop, while loop, switch statements, modules, classes, constructors, functions, objects, and more!
  
### Why it was developed:
 The idea seems complex enough to incorporate a lot of elements we explored in class, and would make for a great addition to my portfolio. Additionally, this is an idea/application I have not explored before, and could be a project that could potentially build out further into fully functional web or mobile application.
 
### Architectural Diagram:
<p align="center">
  <img width="600" alt="image" src="https://github.com/user-attachments/assets/8a9b069b-9415-48e8-a077-01ba6c0a6f4f" />
</p>

### How to run this application:
- Download the repo and save the folder in the appropriate directory or clone the repo using `git clone <repository-url>`: [Git Clone](https://git-scm.com/docs/git-clone)
- Open Ubuntu/Linux terminal and navigate to the directory with the downloaded folder `cd path/to/repo`
- Type `./main.py` in the command line to run the program. If `./main.py` does not work, try running it with Python explicitly `python3 main.py` ~ *(Replace `python3` with your Python version as needed.)*
  
### Challenges:
- Handeling datetime conversions was tricky, especially when generating the calendar with appropriate dates.
- I used a JSON data set instead of a free/demo API. OpenFoodFacts API returned poor results. API Ninjas worked well, but calorie data was hidden behind pay wall. FatSecret required Oauth2 setup which seemed unnecessairly complex.
- I ended up with a lot of redundant code that can be better optimized given enough time.
  
### Future enhancements:
- Can build out the application to be functional outside of a CLI for real world use cases. eg. Web or mobile application.
- Interactive calendar, so that users can click on dates and navigate via calendar buttons or drop-downs instead of manually entering dates.
- Complex activity logging with graphs and other advanced features. Also, more intuitive navigation between menu and sections. Testing (Unit, integration, etc.)
- API integration & connection to a relational database (SQL, PostgreSQL, etc.) 

### Application Preview (Menu(s) & Calendar output)
<table align="center">
  <tr>
    <td><img width="300" alt="image" src="https://res.cloudinary.com/dhoowagsc/image/upload/v1743569956/428762757-950d9643-31c1-463e-b579-94d7e94cde68_wfmdhv.png" /></td>
    <td><img width="300" alt="image" src="https://res.cloudinary.com/dhoowagsc/image/upload/v1743570202/428765694-965dd0d2-94df-4fa8-aaae-bb947fbf57ca_w278is.png" /></td>
    <td><img width="300" src="https://res.cloudinary.com/dhoowagsc/image/upload/v1743570297/428763397-e86d4ed1-6526-4439-a684-b0ddd442487e_ejvgrd.png" /></td>
  </tr>
  <tr>
    <td><img width="200" src="https://res.cloudinary.com/dhoowagsc/image/upload/v1743570203/428763119-3c18a192-01b8-44d4-8bd1-df33dd5eddea_ljumhw.png" /></td>
    <td><img width="200" src="https://res.cloudinary.com/dhoowagsc/image/upload/v1743570202/428763030-b081d3fb-a0db-4541-b2ab-523d678bbfaa_pabq1x.png" /></td>
    <td><img width="200" src="https://res.cloudinary.com/dhoowagsc/image/upload/v1743570202/428763452-136aaa0a-c86f-4b36-8e9c-a86000901007_ocbv3y.png" /></td>
  </tr>
</table>

### Sample Output
<p align="center">
 <img width="851" src="https://res.cloudinary.com/dhoowagsc/image/upload/v1743570202/428763251-5d918997-7bf3-4101-a3cc-0e0b9645630a_fcrakm.png" />
</p
