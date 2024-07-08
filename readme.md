مرحله ی اول : ایجاد اسکیماز برای اعتبار سنجی داده های ارسالی به ای پی آی و دیتابیس

![Screenshot from 2024-07-08 06-35-29](https://github.com/rezamoridi/project-v/assets/118021932/3c43a42f-c19c-4436-951f-8f62884a8d2a)
مرحله ی دوم :‌ ایجاد تیبل های مورد نیاز برای دیتابیس طبق نیازمند. ۱. دانشجو ۲.مدرس ۳. دروس
![Screenshot from 2024-07-08 06-35-52](https://github.com/rezamoridi/project-v/assets/118021932/9e001588-881d-4ad7-9080-a8512ccccbd5)
ایجاد اندپوینت های ای پی آی . طبق اعمال crud که بر روی دیتابیس صصورت میگیرند
![Screenshot from 2024-07-08 06-36-13](https://github.com/rezamoridi/project-v/assets/118021932/9f18abcb-0da4-4ccb-ba4b-0835b32b46a7)


![Screenshot from 2024-07-08 06-36-21](https://github.com/rezamoridi/project-v/assets/118021932/dafca21f-67f8-4f2a-94be-117cb19f0c27)

ایجاد اعمال و توابع crud که در اند پوینت ها تعریف شده اند.
![Screenshot from 2024-07-08 06-37-05](https://github.com/rezamoridi/project-v/assets/118021932/3bbccb4e-02d9-4c37-8f63-30808b0df672)
طبق تعریف عمل crud هر تیبل نیاز به داشتن ۴ نوع تابع برای ساختن، نوشتن، آپدیت کردن و حذف مقادیر در دیتابیس را نیازدارد.
![Screenshot from 2024-07-08 06-37-13](https://github.com/rezamoridi/project-v/assets/118021932/f0474456-ec36-47ca-a38c-0d65f7cf255f)

![Screenshot from 2024-07-08 06-37-22](https://github.com/rezamoridi/project-v/assets/118021932/c56213c8-d689-4e21-b024-235a2280cf2d)
بعد از تعریف مراحل بالا و نیازمندی ها ( اندپوینت ها، اعمال crud ، مدل ها و اسکیماز ) برای دسته بندی اندپوینت ها نیاز به دسته بندی اندپوینت ها داریم.
![Screenshot from 2024-07-08 06-38-42](https://github.com/rezamoridi/project-v/assets/118021932/5443398d-fb8d-448f-b529-df8ee5cf7e4d)

![Screenshot from 2024-07-08 07-01-27](https://github.com/rezamoridi/project-v/assets/118021932/7b95ea65-60df-47b5-bcef-1242da34173c)

بعد از ساختن پکیج روترز ، اندپوینت های هر دسته هارا به صورت جداگانه در یک ماژول پایتونی که به اسم آن دسته میباشد انقال میدهیم و نیازمندی های آن اندپوینت هارا ایمپورت میکنیم. سپس طبق مراحل زیر APIRouter را از fastapi ایمپورت میکنیم و یک اینستنس از آن ساخته و درون هر یک از ماژول های روتر قرار میدهیم. شی حاصل از اینستنس APIRouter را در router ذخیره میکنیم و به جای اینستنس app استفاده میکنیم. 
![Screenshot from 2024-07-08 07-05-59](https://github.com/rezamoridi/project-v/assets/118021932/64908b93-55b4-459f-907c-e0e8b9741e7c)
برای اینکه fastapi بعد از جابه جایی روتر و اپ بتواند اند پوینت هارا شناسایی کند نیاز داریم تا آنها را در فایل config.py که ساختیم include کنیم.
![Screenshot from 2024-07-08 07-08-47](https://github.com/rezamoridi/project-v/assets/118021932/ae430767-35a0-4828-933c-ba6b58c0ea50)
طبق کد های بالا اینستنس اپ که از روی کلاس Fastapi ساخته شده بود را در انجا قرار میدهیم و با استفاده از متود include_router آدرس روتر و تگ مورد نظر را برای آن قرار میدهیم.

