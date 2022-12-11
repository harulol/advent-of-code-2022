import scala.util.*

class Operation(val operand: Char, val right: String | Int):

   private def calc(left: Long, right: Long): Long =
      operand match
         case '+' =>
            left + right
         case '*' =>
            left * right

   def calculateNew(old: Long): Long =
      right match
         case _: String => calc(old, old)
         case v: Int => calc(old, v)

object Operation:

   // Some parsing the operation. Left is always "old" so doesn't need to store.
   def parse(op: String): Operation =
      val arr = op.split(" ") // [old, op, right]

      Try(Integer.parseInt(arr(2))) match
         case Success(value) =>
            Operation(arr(1).charAt(0), value)
         case Failure(_) =>
            Operation(arr(1).charAt(0), arr(2))
   end parse
