Команды в Shell
	from news.models import *

1.Создать двух пользователей (с помощью метода User.objects.create_user('username’)):
user1 = User.objects.create_user(username='Алексей Быстров')
user2 = User.objects.create_user(username='Виктория Репина')

Делал команды ниже вместо верхних, т.к. Юзеры у меня уже были созданы с соответствующими ID:
user1 = User.objects.get(id=12)
user2 = User.objects.get(id=13)

user1.save()
user2.save()

2.Создать два объекта модели Author, связанные с пользователями:
author1 = Author.objects.create(authUser=user1)
a1 = Author.objects.get(id=1)
a1.save()
author2 = Author.objects.create(authUser=user2)
a2 = Author.objects.get(id=2)
a2.save()

3.Добавить 4 категории в модель Category:
Category.objects.create(catName='Спорт')
Category.objects.create(catName='Культура')
Category.objects.create(catName='Политика')
Category.objects.create(catName='Общество')

4.Добавить 2 статьи и 1 новость:
post1 = Post.objects.create(author=author1, typeChoice='NEW', headline='Хоккейные боссы Чехии сели в лужу. Сокрушительный провал хозяев чемпионата мира', text='Международная федерация хоккея (IIHF) отстранила российских спортсменов от участия в двух грядущих чемпионатах мира. В нынешнем году мы не едем в Латвию и Финляндию, а в следующем — в Чехию. Тем временем хозяева ЧМ-2024 вовсю готовятся к знаменательному событию.')

post2 = Post.objects.create(author=author1, typeChoice='ART', headline='Норрис: Я очень критично оцениваю свои выступления', text='В McLaren слабо начали сезон 2023 года и только в третьей гонке во многом благодаря сходу соперников заработали первые очки. Гонщик команды Ландо Норрис рассказал, что самокритика помогает ему поддерживать мотивацию в отсутствии высоких результатов на трассе.')
	
post3 = Post.objects.create(author=author2, typeChoice='ART', headline='Режиссер Клим Шипенко заявил о реакции Тома Круза на его фильм «Вызов»', text='Клим Шипенко, который отныне позиционирует себя первым в мире и в истории режиссером, реально слетавшим в космос, а также снявшим на земной орбите первый на земном шаре художественный фильм, рассказал о том, что именно он думает относительно критиков Запада.')


5.Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий):
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
p1 = Post.objects.get(id=1)
p1.save()
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=2))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=4))
Post.objects.filter(id=1).values('postCategory__catName')
Post.objects.filter(id=2).values('postCategory__catName')
Post.objects.filter(id=3).values('postCategory__catName')

6.Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий):
Comment.objects.create(postComm=p1, userComm=user2, comment='Люблю хоккей')

Comment.objects.create(postComm=Post.objects.get(id=2), userComm=user2, comment='Жду продолжение фильма «вызов» с Томом в главной роли')

Comment.objects.create(postComm=Post.objects.get(id=2), userComm=user1, comment='Ландо, good luck в новом сезоне!')

Comment.objects.create(postComm=Post.objects.get(id=3), userComm=user1, comment='Фильм получился хорошим')

7.Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов:
Comment.objects.get(id=1).like()
Comment.objects.get(id=2).dislike()
Comment.objects.get(id=1).like()
p1.like()
Post.objects.get(id=2).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()

8.Обновить рейтинги пользователей:
a1.update_rating()
a2.update_rating()

9.Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта):
best_rate = Author.objects.order_by('-authorRating')[:1]
for i in best_rate:
	i.authorRating
	i.authUser.username


10.Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье:
r=Post.objects.order_by("-postRating")[:1].values('id')
Post.objects.order_by('-postRating')[:1].values('pubDate', 'author__authUser__username', 'postRating', 'headline'), Post.objects.get(id=r).preview()


11.Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье:
Все комментарии:
Comment.objects.filter().values('dateOfComment', 'userComm__username', 'commentRating', 'comment')
Комментарий лучшего по рейтингу:
Comment.objects.order_by('-commentRating')[:1].values('dateOfComment', 'userComm__username', 'commentRating', 'comment')

