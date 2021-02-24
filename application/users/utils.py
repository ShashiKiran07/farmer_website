import secrets
import os
# from PIL import Image
# from flask import url_for, current_app
import boto3

s3 = boto3.client(
    's3',
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
)

# def save_picture(form_picture):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(form_picture.filename)
#     picture_fn = random_hex + f_ext
#     # picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
#     picture_path = os.path.join("https://raithu-nestham.s3.amazonaws.com/", 'static/profile_pics', picture_fn)
#     # output_size = (125,125)
#     i = Image.open(form_picture)
#     # i.thumbnail(output_size)
#     i.save(picture_path)

#     return picture_fn

def upload_to_s3(form_picture, bucket_name, acl='public-read'):
    _, f_ext = os.path.splitext(form_picture.filename)
    random_hex = secrets.token_hex(8)
    form_picture.filename = random_hex+f_ext
    try:
        s3.upload_fileobj(
            form_picture,
            bucket_name,
            'static/profile_pics/' + form_picture.filename,
            ExtraArgs={
                "ACL":acl,
                "ContentType":form_picture.content_type
            }
        )
    
    except Exception as e:
        print("Something Happened: ", e)
        return e
    
    return form_picture.filename