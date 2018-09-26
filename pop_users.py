from django.contrib.auth.models import User

users = [
["lulaman","8080ujht!@@gJB"],
["simphiwe","88hgtyY78uNNH!"],
["luyandal","ekE88:&3s)s-=*(s"],
["maureens","QeehSR[f96N(W?T~"],
["nhlanhlam","{dY;b^2`TW5qa?Cz"],
["lindiwem","Nz8s=WLg8S.:#&W_"],
["meisiel","X2%Q'@A5C>pB;xB'"],
["glorym","T8xX6bVbXsxT11x5"],
]

for user in users:
    user=User.objects.create_user(user[0], user[1])
    user.is_staff=True
    user.save()
