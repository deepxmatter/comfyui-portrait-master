# PORTRAIT MASTER
# Created by AI Wiz Art (Stefano Flore)
# Version: 1.0

import os

script_dir = os.path.dirname(__file__)

# read txt file

def pmReadTxt(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        values = [line.strip() for line in lines]
        return values

# setup vars

shot_list = pmReadTxt(os.path.join(script_dir, "lists/shot_list.txt"))
shot_list.sort()
shot_list = ['-'] + shot_list

gender_list = pmReadTxt(os.path.join(script_dir, "lists/gender_list.txt"))
gender_list.sort()
gender_list = ['-'] + gender_list

nationality_list = pmReadTxt(os.path.join(script_dir, "lists/nationality_list.txt"))
nationality_list.sort()
nationality_list = ['-'] + nationality_list

hair_style_list = pmReadTxt(os.path.join(script_dir, "lists/hair_style_list.txt"))
hair_style_list.sort()
hair_style_list = ['-'] + hair_style_list

class PortraitMaster:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "shot": (shot_list, {
                    "default": shot_list[0],
                }),
                "shot_weight": ("FLOAT", {
                    "default": 0,
                    "step": 0.05,
                    "min": 0,
                    "max": 1.75,
                    "display": "slider",
                }),
                "gender": (gender_list, {
                    "default": gender_list[0],
                }),
                "hair_style": (hair_style_list, {
                    "default": hair_style_list[0],
                }),
                "disheveled": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": 1.50,
                    "step": 0.05,
                    "display": "slider",
                }),
                "nationality_1": (nationality_list, {
                    "default": nationality_list[0],
                }),
                "nationality_2": (nationality_list, {
                    "default": nationality_list[0],
                }),
                "nationality_mix": ("FLOAT", {
                    "default": 0.5,
                    "min": 0,
                    "max": 1,
                    "step": 0.05,
                    "display": "slider",
                }),
                "age": ("INT", {
                    "default": 30,
                    "min": 18,
                    "max": 90,
                    "step": 1,
                    "display": "slider",
                }),
                "freckles": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": 1.50,
                    "step": 0.05,
                    "display": "slider",
                }),
                "skin_details": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": 1.50,
                    "step": 0.05,
                    "display": "slider",
                }),
                "skin_pores": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": 1.50,
                    "step": 0.05,
                    "display": "slider",
                }),
                "moles": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": 1.50,
                    "step": 0.05,
                    "display": "slider",
                }),
                "skin_imperfections": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": 1.50,
                    "step": 0.05,
                    "display": "slider",
                }),
                "eyes_details": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": 1.50,
                    "step": 0.05,
                    "display": "slider",
                }),
                "iris_details": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": 1.50,
                    "step": 0.05,
                    "display": "slider",
                }),
                "circular_iris": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": 1.50,
                    "step": 0.05,
                    "display": "slider",
                }),
                "circular_pupil": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": 1.50,
                    "step": 0.05,
                    "display": "slider",
                }),
                "prompt_start": ("STRING", {
                    "multiline": True,
                    "default": "raw photo, (realistic:1.5)"
                }),
                "prompt_additional": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "prompt_end": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
            }
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "pm"

    CATEGORY = "AI WizArt"

    def pm(self, shot, shot_weight=1, gender="-", nationality_1="-", nationality_2="-", nationality_mix=0.5, age=30, hair_style="-", disheveled=0, freckles=0, skin_pores=0, skin_details=0, moles=0, skin_imperfections=0, eyes_details=1, iris_details=1, circular_iris=1, circular_pupil=1, prompt_additional="", prompt_start="", prompt_end=""):

        prompt = []

        if gender == "-":
            gender = ""
        else:
            gender = gender + " "

        if nationality_1 != '-' and nationality_2 != '-':
            nationality = f"[{nationality_1}:{nationality_2}:{nationality_mix}] "
        elif nationality_1 != '-':
            nationality = nationality_1 + " "
        elif nationality_2 != '-':
            nationality = nationality_2 + " "
        else:
            nationality = ""

        if prompt_start != "":
            prompt.append(f"{prompt_start}")

        if shot != "":
            prompt.append(f"({shot}:{round(shot_weight, 2)})")

        prompt.append(f"{nationality}{gender}{round(age)}-years-old")

        if hair_style != "-":
            prompt.append(f"({hair_style} hairstyle:1.25)")

        if disheveled != "-":
            prompt.append(f"(disheveled:{round(disheveled, 2)})")

        if prompt_additional != "":
            prompt.append(f"{prompt_additional}")

        if skin_details > 0:
            prompt.append(f"(skin details, skin texture:{round(skin_details, 2)})")

        if skin_pores > 0:
            prompt.append(f"(skin pores:{round(skin_pores, 2)})")

        if skin_imperfections > 0:
            prompt.append(f"(skin imperfections:{round(skin_imperfections, 2)})")

        if freckles > 0:
            prompt.append(f"(freckles:{round(freckles, 2)})")

        if moles > 0:
            prompt.append(f"(skin pores:{round(moles, 2)})")

        if eyes_details > 0:
            prompt.append(f"(eyes details:{round(eyes_details, 2)})")

        if iris_details > 0:
            prompt.append(f"(iris details:{round(iris_details, 2)})")

        if circular_iris > 0:
            prompt.append(f"(circular iris:{round(circular_iris, 2)})")

        if circular_pupil > 0:
            prompt.append(f"(circular pupil:{round(circular_pupil, 2)})")

        if prompt_end != "":
            prompt.append(f"{prompt_end}")

        prompt = ", ".join(prompt)
        prompt = prompt.lower()

        print("Portrait Master as generate the prompt:")
        print(prompt)

        return (prompt,)
    
NODE_CLASS_MAPPINGS = {
    "PortraitMaster": PortraitMaster
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PortraitMaster": "Portrait Master by AI WizArt"
}