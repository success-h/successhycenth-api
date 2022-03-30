
from django.db import models
class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Works(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=250)
    source = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')
    tags = models.ManyToManyField(Tag)
    id = models.AutoField(primary_key=True, unique=True)

    def __str__(self):
        return self.name


# [
#     {
#         "name": "Transfer Wise",
#         "description": "beautiful clone of the transferwise.com. homepage I attempted the design and most functionalities present on the website.",
#         "link": "https://transferwise.netlify.app/",
#         "image": "https://res.cloudinary.com/dp3a4be7p/image/upload/v1/media/portfolio/images/transferwise_yenq7s",
#         "tags": [
#             {
#                 "name": "React.js"
#             },
#             {
#                 "name": "Next.js"
#             },
#             {
#                 "name": "Tailwindcss"
#             }
#         ]
#     },
#     {
#         "name": "Medium Clone",
#         "description": "attempt the clone of  beautiful Medium blog website where people write to help, inspire and connect to each other",
#         "link": "https://medium-clone-guml9etmc-success-h.vercel.app/",
#         "image": "https://res.cloudinary.com/dp3a4be7p/image/upload/v1/media/portfolio/images/medium_kd1l68",
#         "tags": [
#             {
#                 "name": "React.js"
#             },
#             {
#                 "name": "Next.js"
#             },
#             {
#                 "name": "Tailwindcss"
#             }
#         ]
#     },
#     {
#         "name": "Crown Clothing",
#         "description": "E-commerce clothing store with full functionalities of Modern Front-End web app, features includes payment with stripe, redux and more",
#         "link": "https://crwn-clothing-navy-ten.vercel.app/",
#         "image": "https://res.cloudinary.com/dp3a4be7p/image/upload/v1/media/portfolio/images/crown_hzb4dp_uw5xaa",
#         "tags": [
#             {
#                 "name": "React.js"
#             },
#             {
#                 "name": "Sass"
#             },
#             {
#                 "name": "redux"
#             }
#         ]
#     }
# ]