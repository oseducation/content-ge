# FillWorld

 პრობლემა:
 ```
  კარელი დგას 1x1 უჯრაზე, შეავსებინეთ მას მთელი სამყარო თითო ბრილიანტით. ანუ მთელ
  სამყაროში ყველა უჯრაზე უნდა იდოს ზუსტად ერთი ბრილიანტი. ჩათვალეთ რომ საწყისი
  სამყარო ცარიელი არ არის და გარკვეულ(ჩვენთვის უცნობ) უჯრებში თითო(მხოლოდ ერთი)
  ბრილიანტი დევს. ამასთან გაითვალისწინეთ, რომ სამყაროს ზომები თქვენთვის უცნობია და
  თქვენი პროგრამა უნდა მუშაობდეს ნებისმიერი ზომის სამყაროსათვის.
 ```

 ## პრობლემის გადაჭრის გზა
მოდი კარელი ვატაროტ ზიგზაგურად, რათა ბევრი არ ვაწვალოთ და ერთსადაიმავე უჯრაზე ორჯერ არ მოხვდეს. პრობლემა შეიძლება დავყოთ ოთხ ნაწილად

 * ქუჩის გავლა
 * ყოველ უჯრაზე ბრილიანტების განთავსება
 * ზიგზაგურად მომდევნო ქუჩაზე გადასვლა
 * მიხვედრა, რომ ყველა უჯრა გავიარეთ და პროგრამის დამთავრება

 ---

 ### მთლიანი ქუჩის გავლის პრობლემას გადავჭრით შემდეგი საშაულებით
 1. გამოვიყენოთ `frontIsClear()` მეთოდი.
 2. გამოვიყენოთ `while` ციკლი.
 3. წინაღობის შემოწმების შემდგომ, გადავიდეთ ერთი უჯრით წინ `move()` მეთოდის საშუალებით.

 ### ბრილიანტის დადების პრობლემა
 შევამოწმოთ არის თუ არა მაგ უჯრაზე ბრილიანტი `noBeepersPresent()`-ის საშუალებით და მხოლოდ იმ შემთხვევაში დავდოთ ბრილიანტი თუ ჯერ არ დევს.

 ### მაღლა ასვლა
 ჩვენ გვინდა, რომ შევტრიალდეთ ჩრდილოეთისკენ, ამისთვის გასათვალისწინებელია ორი შემთხვევა
 1. როცა მოძრაობა დავამთავრეთ სახით აღმოსავლეთისკენ
 2. დასავლეთისკენ
 პირველ შემთხვევაში გვჭირდება მარცხნივ მოტრიალება, მეორეში კი მარჯვნივ
 ამას ვარკვევთ `facingEast()`-ის საშუალებით და შესაბამისად ვბრუნდებით

 მეორე მომენტია, მოძრაობის მიმართულების შეცვლა
 ანუ, თუ მოვეცი მარცხნიდან მარჯვნივ, შემდეგი სტრიქონი უნდა შევავსო მარჯვნიდან მარცხნივ და პირიქით

 ამას ვაგვარებთ შემდეგნაირად, თუ ჩემი მარცხენა მხარეა დაბლოკილი, ესეიგი მარჯვნივ უნდა შევტრიალდე
 და ისე განვაგრძნო სამყაროს შევსება, ხოლო თუ მარჯვენა, პირიქით.

 ## რატომ იმუშავებს ეს ამოხსნა ყველა სამყაროსთვის?
 ჩვენი კოდი არ არის დამოკიდებული სამყაროს ზომებზე, გამოყენებული გვაქვს ვაილ ციკლი რომლისთვისაც მნიშვნელობა
 არ აქვს რა იქნება სამყაროს განზომილებები, მაინც ერთსა და იმავე რამეს გააკეთებს

