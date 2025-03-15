# StepWise Documentation

### How To Setup The MTurk Task.

1. Go to [https://requester.mturk.com/signin_options](https://requester.mturk.com/signin_options) and create an account 

![image.png](image.png)

After Logging in with your credentials, You will be redirected to the dashboard

![image.png](image%201.png)

1. Now, click on New Project

![image.png](image%202.png)

1. Select the video classification template

![image.png](image%203.png)

1. Select On create Project

![image.png](image%204.png)

1. edit the Title Description  and keywords suitable 

![image.png](image%205.png)

here,
**Title :** Classify which of the two given scenes is well aligned with the prompt

**Description :** The scenes below were created by a text-to-scene model from the given prompt. Please consider both the prompt and the scenes in your response.

**Keywords :**  video, classification

1. Edit the reward rate and further details about the task

![image.png](image%206.png)

1. Choose the worker requirements

![image.png](image%207.png)

1. Click on design layout

![image.png](image%208.png)

1. You will be redirected to the following page

![image.png](image%209.png)

1. In the html editor paste the following code :

```html
<!DOCTYPE html>
<html>
<head>
    <title>3D Scene Evaluation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
            text-align: center;
        }
        .container {
            background: white;
            max-width: 900px;
            margin: auto;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #333;
        }
        .video-container {
            display: flex;
            justify-content: space-between;
            margin: 20px 0;
            gap: 20px;
        }
        video {
            width: 100%;
            max-width: 420px;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .question {
            background: #f9f9f9;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            text-align: left;
        }
        .question p {
            margin: 5px 0;
        }
        input[type="submit"] {
            background: #007bff;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.3s;
        }
        input[type="submit"]:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>3D Scene Evaluation Task</h2>
        
        <p><strong>Prompt:</strong> ${prompt}</p>

        <div class="video-container">
            <div>
                <h3>Scene A</h3>
                <video controls>
                    <source src="${video_A_url}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            <div>
                <h3>Scene B</h3>
                <video controls>
                    <source src="${video_B_url}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
        </div>

        <h3>Survey Questions</h3>
        
        <div class="question">
            <p>1. In which scene are the room and objects sized more appropriately?</p>
            <label><input type="radio" name="Q1" value="A" required> Scene A</label>
            <label><input type="radio" name="Q1" value="B"> Scene B</label>
        </div>

        <div class="question">
            <p>2. In which scene are the objects arranged more naturally?</p>
            <label><input type="radio" name="Q2" value="A" required> Scene A</label>
            <label><input type="radio" name="Q2" value="B"> Scene B</label>
        </div>

        <div class="question">
            <p>3. Overall, which scene is more aesthetically pleasing?</p>
            <label><input type="radio" name="Q3" value="A" required> Scene A</label>
            <label><input type="radio" name="Q3" value="B"> Scene B</label>
        </div>

        <div class="question">
            <p>4. Overall, which scene is better?</p>
            <label><input type="radio" name="Q4" value="A" required> Scene A</label>
            <label><input type="radio" name="Q4" value="B"> Scene B</label>
        </div>

        <div class="question">
            <p>5. In which scene are the objects arranged more in accordance with the caption/prompt?</p>
            <label><input type="radio" name="Q5" value="A" required> Scene A</label>
            <label><input type="radio" name="Q5" value="B"> Scene B</label>
        </div>

        <div class="question">
            <p>6. In which scene are the object-object relations more in accordance with the caption?</p>
            <label><input type="radio" name="Q6" value="A" required> Scene A</label>
            <label><input type="radio" name="Q6" value="B"> Scene B</label>
        </div>
        <input type="submit" value="Submit">
    </div>
</body>
</html>

```

1. click on preview

![image.png](image%2010.png)

1. You can preview the task window and when satisfied, click on finish

![image.png](image%2011.png)

1. click on publish batch in the dashboard

![image.png](image%2012.png)

1. A Pop up will show up where you can upload the csv file 

![image.png](image%2013.png)

1. click on choose file and upload the given file :

    
    [scene_data_s3.csv](scene_data_s3.csv)
    

1. click on upload

![image.png](image%2014.png)

1. You can preview the survey

![image.png](image%2015.png)

1. You will get a cost summary ( NOTE THE REWARD AMOUNT HASN’T BEEN FINALISED YET)

![image.png](image%2016.png)

NEXT STEPS NEEDS TO BE DISCUSSED

NOTE THIS IS THE FEE STRUCTURE MTURK CHARGES 

![image.png](image%2017.png)