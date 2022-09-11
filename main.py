import easyocr

def text_recognition_to_console(image_path):
    reader = easyocr.Reader([language])
    result = reader.readtext(image_path, detail=0)
    print(result)

def text_recognotion(image_path, new_file_name):
    reader = easyocr.Reader([language])
    result = reader.readtext(image_path,detail=0)

    with open(new_file_name, "w") as file:
        for line in result:
            file.write(f"{line}\n\n")


image_path = input("Input path of image: ")
question = input("If you want to get text as file input 0, if you want to get a text in a console input 1: ")
language = input("Select language of text in image (ru, en, ua etc): ")

if question == "0":
    new_file_name = input("Insert name for textfile: ")
    text_recognotion(image_path=image_path, new_file_name=new_file_name)
elif question == "1":
    text_recognition_to_console(image_path=image_path)
else:
    print("You have inserted wrong number!")


