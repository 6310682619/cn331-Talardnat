# TU-TALARDNAT

Video How to use our website<br>
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=DJVMMIAhhWY)

Link to heroku<br>
[![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)](https://tu-talardnat.herokuapp.com/)

-------
## Installation

1. Clone GitHub repository.

    **RUN:**
    ```console
    git clone https://github.com/6310682619/cn331-Talardnat.git
    ```

2. Create a **virtual environment**.

    Linux/MacOS:

   **RUN:**

   ```console
   python3 -m venv venv
   ```

   Windows:

   **RUN:**

   ```console
   python -m venv venv
   ```

3. Activate virtual environment.

    Linux/MacOS:

   **RUN:**

   ```console
   . ./venv/bin/activate
   ```

   Windows:

   **RUN:**

   ```console
   . ./venv/Scripts/activate
   ```

4. Install requirements for this project.

   **RUN:**

    ```console
    python install -r requirements.txt
    ```
5. Change to directory that contain file **manage.py**

    **RUN:**

    ```console
    cd /Talardnat
    ```

6. Run server.

    **RUN:**

    ```console
    python manage.py runserver
    ```

7. Open project using browser.

   Open URL: [**`https://127.0.0.1:8000`**](https://127.0.0.1:8000)


## Usage

### **USER PART**

[![Homepage](Talardnat/images/2022-11-26.png)](Talardnat/images/2022-11-26.png)
เมื่อเข้าหน้าเว็บไซต์จะปรากฏหน้าหลักของตลาด ซึ่งจะมีให้เลือกว่าจะเป็น ผู้ซื้อ (Shopper) หรือผู้ขาย (Seller) และมีปุ่ม rate us และ about us ที่มุมล่างขวา

[![About Us](Talardnat/images/about.png)](Talardnat/images/about.png)
หน้า About Us จะแสดงข้อมูลของผู้พัฒนาเว็บไซต์ รวมถึง link ไปยัง GitHub repository และ Pivotal Tracker

[![Rate Us](Talardnat/images/rate.png)](Talardnat/images/rate.png)
หน้า Rate Us ผู้ใช้ทุกคนสามารถประเมิณความพึงพอใจในการใช้งานเว็บไซต์ได้ โดยจะต้องทำการ login ก่อน


#### CUSTOMER
1. เมื่อเข้ามาที่หน้า shopper จะปรากฏหน้า login ซึ่ง user สามารถเข้าได้ด้วยการใส่ username และ password
[![Customer Login](Talardnat/images/cuslog.png)](Talardnat/images/cuslog.png)
หาก user ยังไม่มีบัญชี สามารถกดไปที่ Sign Up as Customer เพื่อสร้างบัญชีได้
[![Customer Signup](Talardnat/images/cussign.png)](Talardnat/images/cussign.png)
2. หลังจาก login สำเร็จจะเข้าไปที่หน้า Your Profile : Customer ที่จะแสดงข้อมูลของเจ้าของบัญชี
[![Customer Profile](Talardnat/images/cuspro.png)](Talardnat/images/cuspro.png)
3. กดปุ่ม SHOP จะเข้าสู่หน้า catagory ซึ่งจะมีให้เลือกระหว่างจะไปโซน food(ขายอาหาร) หรือ utensil(ขายของใช้) โดยที่ตรงมุมล่างซ้ายมีปุ่มที่สามารถไปหน้า Home, Rate us, About us, My order และ log out
[![Category](Talardnat/images/category.png)](Talardnat/images/category.png)
4. หากกดไปที่ปุ่ม food จะเข้าไปที่หน้า talard หน้านั้นจะเรียงร้านค้า ซึ่งส่วนหน้าจะเป็นร้านขายอาหารแล้วส่วนท้ายจะเป็นร้านขายของใช้ 
[![Food](Talardnat/images/food.png)](Talardnat/images/food.png)
หากกดไปที่ปุ่ม utensil ร้านขายของใช้จะเรียงอยู่ที่ส่วนหน้า แล้วมีร้านขายอาหารอยู่ในส่วนท้าย
โดยด้านล่างจะมีปุ่ม My order เพื่อเข้าไปหน้า order ของฉันทันที
[![Utensil](Talardnat/images/uten.png)](Talardnat/images/uten.png)
5. เมื่อกดเข้าไปในร้าน จะเจอกับหน้าร้าน และ Product ของร้านนั้นๆ เราสามารถเลือกสินค้าที่ต้องการ ใส่จำนวน แล้วกดปุ่ม add แล้วรายการสินค้านั้นจะไปปรากฏที่หน้า my order 
6. เมื่อเลื่อนลงไปข้างล่างจะเจอกับ review ของร้านค้าร้านนี้ ซึ่งเราสามารถเขียน review ให้ร้านค้าร้านนี้ได้หากเราเคยซื้อของจากร้านค้าร้านนี้แล้ว โดยต้องกดเข้าไปที่ปุ่ม write your review แล้วจะมีหน้าต่างเด้งขึ้นมาให้เขียน review ซึ่ง review ของเรา จะไปปรากฏอยู่ข้างล่าง และถ้ามี review ที่ลูกค้าคนอื่นเขียนอยู่เราก็สามารถอ่านได้
7. หลังจากเลือกซื้อสินค้าที่ต้องการเรียบร้อย ก็กดเข้าไปที่ปุ่ม my order เพื่อเข้าไปดูสินค้าที่เราเลือกในหน้า order ของฉัน ในส่วนของ Shopping cart คือตารางของสินค้าที่เราเลือก add เข้ามา แต่ยังไม่จ่ายเงิน
8. หากต้องการชำระค่าสินค้า ก็กดที่ปุ่ม Check Out แล้วจะมีหน้าต่างเด้งขึ้นมาให้ใส่ข้อมูลของบัตรที่จะใช้ชำระเงิน หลังจากชำระเงินเรียบร้อย สินค้าของเราจะเข้าไปอยู่ในตาราง Carry out ซึ่งเป็นตารางของสินค้าที่ชำระเงินแล้ว แต่สินค้ายังไม่มาถึงมือลูกค้า
9. เมื่อลูกค้าได้รับสินค้าแล้วก็ต้องกด recieved เพื่อยืนยันว่าได้รับสินค้าแล้ว จากนั้นสินค้าที่ยืนยันว่าได้รับแล้วจะไปอยู่ที่ Finished เพื่อแสดงว่ากระบวนการซื้อสินค้านี้เสร็จสิ้นแล้ว

#### SELLER

1. เมื่อเข้ามาที่หน้า seller จะปรากฏหน้า login ซึ่ง user สามารถเข้าได้ด้วยการใส่ username และ password หาก password หรือ user ไม่ถูกต้องจะให้ใส่ username และ password อีกครั้ง และมีประโยค "Invalid credentials." ขึ้นมาเตือน
หาก user ยังไม่มีบัญชี สามารถกดไปที่ Sign Up as Seller เพื่อสร้างบัญชีได้
2.หากใส่ password และ user ในหน้า login ถูกต้อง จะปรากฎหน้า Profile ซึ่งจะแสดงข้อมูลของ User ได้แก่ Name Username และ Email จาก Profile เราสามารถ เข้าไปที่ Myshop ได้
3. ที่หน้า Myshop จะแสดง My shop list ซึ่งเป็นร้านค้าต่างๆของเรา สามารถเลือกกดร้านค้าที่เราจะเข้าไปจัดการได้
หรือหากอยากเพิ่มร้านค้าตัวเองก็สามารถกดเพิ่มร้านค้าที่ ADD SHOP ด้านล่างสุดได้
4. เมื่อเข้ามาที่หน้าร้านค้าที่เลือก (MYSHOP) ก็จะสามารถจัดการกับร้านค้าของเราได้ โดยมีปุ่มให้เลือก 4 ปุ่ม คือ product, edit, review, add queue และมีรายการ order จากที่ลูกค้ากดเลือกซื้อแสดงอยู่ด้านล่างของหน้าเพจ โดยมี
Aleready paid คือรายการสินค้าที่จ่ายเงินซื้อเรียบร้อนแล้ว
New Order คือ รายการสินค้าที่ถูกใส่ไว้ในตระกร้าแล้ว แต่ยังไม่ได้จ่ายเงิน
Recieved Order คือรายการสินค้าที่ลูกค้ากดว่าได้รับแล้ว
5. เมื่อเข้าไปที่หน้า My product จากหน้า My shop แล้ว เราก็จะสามารถ ดูรายการสินค้า แก้ไขรายละเอียดสินค้า ลบสินค้า หรือ เพิ่มสินค้าได้
6. เมื่อเข้าไปที่หน้า Edit detail จากหน้า My shop แล้ว เราก็จะสามารถแก้ไขรายละเอียดของร้านค้าต่างๆได้ ทั้ง Name, Category, In interact, Ex interact, Shop image, Payment
7. เมื่อเข้าไปที่หน้า My Review จากหน้า My shop เราก็จะสามารถเห็นดาว และรีวิวจากลูกค้าที่มารีวิวร้านของเราได้
8. เมื่อเข้าไปที่หน้า Add Queue จากหน้า My shop เราจะสามารถกด Add Queue ร้านเพื่อไปขายจริงได้ โดยจะแบ่งเป็นรอบๆตามวันที่ที่กำหนด หากอยากยกเลิก Queue ก็สามารถกด Cancle Queue ที่ด้านบนสุดได้

### **ADMIN PART**
มื่อเข้าหน้าเว็บไซต์จะปรากฏหน้าหลักของตลาด ต้องไปที่ URL เพื่อเพิ่ม /admin ต่อท้าย URL แล้วก็จะสามารถเข้าหน้า log in ของ admin ได้ ซึ่งต้องใช้ username และ password ของ admin ในการเข้าหน้า admin
1. ผู้ที่เป็น admin สามารถดูได้ว่าใครเป็น user ของเว็บบ้าง โดยกดเข้าไปดูที่ Users รวมถึงสามารถเพิ่มและลบ user ได้
2. ผู้ที่เป็น admin สามารถดูได้ว่าใครเป็น user ฝั่ง customer บ้าง โดยการกดไปที่ Profile และสามารเพิ่มและลบ user ที่เป็น customer ได้ รวมถึงสามารถแก้ไขข้อมูลของ user แต่ละคนได้ด้วย
3. ผู้ที่เป็น admin สามารถดูได้ว่า user ที่เป็น customer สั่งสินค้าอะไรบ้าง จากร้านค้าไหนโดยไปดูที่ My order
4. ผู้ที่เป็น admin สามารถดูได้ว่า user ที่เป็น seller ขายสินค้าอะไรบ้างในร้านไหนโดยไปดูที่ Products
5. ผู้ที่เป็น admin สามารถจัดการ round ต่าง ๆ ได้ โดยกดไปดูที่ Rounds ซึ่ง admin สามารถเพิ่มลด round ได้ รวมถึงแก้ไขร้านค้าที่ต่อ queue ใน round นั้น ๆ ได้
6. ผู้ที่เป็น admin สามารถดูได้ว่ามีร้านค้าอะไรในเว็บบ้างและร้านค้านั้นเป็นของ user ฝั่ง seller คนไหน โดยกดไปดูที่ Shop_details
7. ผู้ที่เป็น admin สามารถดูได้ว่าใครเป็น user ฝั่ง seller บ้าง โดยการกดไปที่ Seller_details และสามารเพิ่มและลบ user ที่เป็น seller ได้ รวมถึงสามารถแก้ไขข้อมูลของ user แต่ละคนได้ด้วย
8. ผู้ที่เป็น admin สามารถดูได้ว่ามี user คนไหนมาให้ Rate เว็บไซต์บ้าง และเขาให้ Rate ไว้ว่าอย่างไร โดยกดไปดูที่ Rate uss
9. ผู้ที่เป็น admin สามารถดูได้ว่ามี user ที่เป็น customer คนไหนเขียน review ให้ร้านค้าไหนบ้าง และเขียนไว้ว่าอย่างไร โดยการกดเข้าไปดูที่ Reviews


-----
## TEAM MEMBERS

- 6310611014 - ชวันรัตน์ ทรัพย์เบญจภาคิน
- 6310682601 - มุนินทร์ วุฒิพงศ์วรกิจ
- 6310682619 - เขมิกา วีรกุลวัฒนา
- 6310682650 - รัญชนา ศุภเสวต
