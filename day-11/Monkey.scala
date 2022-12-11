import scala.collection.mutable

class Monkey(val id: Int, val starting: mutable.ArrayBuffer[Long], val operation: Operation, val test: DivisibleTest):
   var inspections: Long = 0

   def inspect(item: Long, divide: Boolean, modulo: Long): (Long, Int) =
      inspections += 1
      var newWorry = operation.calculateNew(item)
      if divide then newWorry /= 3

      newWorry %= modulo

      (newWorry, test.test(newWorry))

   override def toString: String =
      s"Monkey(id=$id,starting=${starting.toString()},operation=(${operation.operand},${operation.right}),test=(${test.by},${test.throwTrue},${test.throwFalse}))"

object Monkey:
   def parse(name: String, items: String, operation: String, divisibility: mutable.ArraySeq[String]): Monkey =
      val id = Integer.parseInt(name.replace(":", "").split(" ").last)
      val startingItems = items.split(": ").last.split(", ").map(java.lang.Long.parseLong).to(mutable.ArrayBuffer)
      val op = Operation.parse(operation.split(" = ").last)
      val div = DivisibleTest.parse(divisibility(0), divisibility(1), divisibility(2))
      Monkey(id, startingItems, op, div)
