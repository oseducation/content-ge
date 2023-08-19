# NumberOfDivisors
პრობლემა:
```
მომხმარებელს შეყავს მთელი რიცხვი n, პროგრამამ უნდა დაბეჭდოს n ის გამყოფების რაოდენობა
```
## პრობლემის გადაჭრის ხერხები:
1.  მივყვეთ ეტაპობრივად. პირველ რიგში ცხადია შეგვყავს რიცხვი `readInt()` მეთოდით და ვრწმუნდებით ეს რიცხვი ნატურალურია თუ არა. დაგვჭირდება `int`-ტიპის ცვლადი (ჩვენს შემთხვევაში `cnt`), რაშიც შევინახავთ გამყოფების რაოდენობას. გამყოფების დასათვლელად კი `for` ციკლით გადავუყვებით 1-დან `num`-ის ჩათვლით რიცხვებს და ვამოწმებთ თითოეული იტერაციის დროს `num` თუ იყოფა `i` ცვლადზე უნაშთოდ, დადებითი პირობის შემთხვევაში გამოყოფების რაოდენობას ვზრდით - `cnt++`. საბოლოოდ, ჩვენმა მეთოდმა უნდა დააბრუნოს `cnt` ცვლადს.
2.  აგრეთვე არსებობს გაუმჯობესებული ვერსია, რომელშიც `for` ციკლში იტერაციები გრძელდება შემოსული რიცხვის კვადრატულ ფესვამდე - `int sqrtN`. ეს რიცხვი მივიღეთ `(int) Math.sqrt(num)` მეთოდით. ეს მეთოდი აბრუნებს `double` ტიპის მნიშვნელობას და არ უნდა დაგვავიწყდეს მისი დაკასტვა მთელ რიცხვზე. თითოეული იტერაციის დროს თუ `num` რიცხვი უნაშთოდ იყოფა `i` ცვლადზე გამყოფების რაოდენობას ვზრდით ორით - `cnt += 2`. თუ `num ` `i`-ზე გაიყო უნაშთოდ ესე იგი ამ გაყოფით ვიღებთ რიცხვს, რომელიც მოქცეულია [`sqrtN`, `num`] შუალედში და ამ რიცხვზეც `num` უნაშთოდ გაიყოფა, სწორედ ამიტომ გამყოფების რაოდენობას ვზრდით 2-ით. ამის გამო ვზოგავთ იტერაციებს და მხოლოდ `sqrtN`-ის ჩათვლით გადავუყვებით რიცხვებს `for` ციკლში და ავტომატურად ვზრდით იმ გამყოფების რაოდენობას, რომლებიც მოქცეულია [`sqrtN`, `num`] - შუალედში. ამ ხერხით ამოხსნისას გასათვალისწინებელია ერთი დეტალი, თუ კი `sqrtN`-ის კვადრატი ზუსტად ტოლია `num`-ის, ეს ნიშნავს, რომ ბოლო იტერაციაზე, როდესაც `i = sqrtN` ერთით ზედმეტ გამყოფს მიამატებს ეს მეთოდი, ამიტომ უნდა შევამოწმოთ ამ შემთხვევაზე და ერთი გამოვაკლოთ გამყოფების რაოდენობას. რასაც ვაკეთებთ კოდის შემდეგ ნაწილში:
```java
if (sqrtN * sqrtN == num) {
   cnt--;
}
```

## შესაძლო შეცდომები:
- უმეტეს შემთხვევებში `for`ციკლში `i` ცვლადს ვანიჭებთ 0-ს და ისე ვიწყებთ იტერირებას, მაგრამ ჩვენს შემთხვევაში ეს შეცდომა იქნება, რადგან მეთოდი 0-ზე შეამოწმებს იყოფა თუ არა.
- აგრეთვე `for` ციკლში პირველ შემთხვევაში რიცხვებს უნდა გადავუყვეთ `num`-ის ჩათვლის, ანუ პირობა გვექნება `i <= num`, რადგან თავისი თავიც მივათვალოთ გამყოფების რაოდენობას.
- მეორე ხერხით ამოხსნისას შეიძლება დაგვავიწყდეს ერთის გამოკლება `cnt`-თვის, როდესაც `sqrtN*sqrtN == num`, ეს იქნება შეცდომა, რადგან ამ მეთოდით შემოწმებისას ჩვენ ვუმატებდით 2 გამყოფს ერთი თვითონ `i` და მეორე `num / i`, ამ კონკრეტულ შემთხვევაში კი ეს ორი რიცხვი ერთმანეთის ტოლია და მხოლოდ ერთი გამყოფი უნდა მივათვალოთ.