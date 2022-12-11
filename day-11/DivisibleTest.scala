class DivisibleTest(val by: Int, val throwTrue: Int, val throwFalse: Int):
   def test(value: Long): Int =
      if value % by == 0 then
         throwTrue
      else throwFalse

object DivisibleTest:
   def parse(test: String, ifTrue: String, ifFalse: String): DivisibleTest =
      val number = Integer.parseInt(test.trim.split(" ").last)
      val throwTrue = Integer.parseInt(ifTrue.trim.split(" ").last)
      val throwFalse = Integer.parseInt(ifFalse.trim.split(" ").last)
      DivisibleTest(number, throwTrue, throwFalse)
