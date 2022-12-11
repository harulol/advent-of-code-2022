import java.io.{BufferedReader, File, FileReader}
import scala.collection.mutable

var modulo: Long = 1

def cycle(monkeys: mutable.ArrayBuffer[Monkey], divide: Boolean = false): Unit =
  monkeys.foreach(m => {
    m.starting.foreach(item => {
      val (it, target) = m.inspect(item, divide, modulo)
      monkeys(target).starting += it
    })
    m.starting.clear()
  })

@main
def main(): Unit =
  val monkeys = mutable.ArrayBuffer[Monkey]()
  val monkeys2 = mutable.ArrayBuffer[Monkey]()

  // Read file and parse monkeys!!
  val file = File("./input.txt")
  val reader = BufferedReader(FileReader(file))
  var guard = true

  while guard do
    val monkey = reader.readLine()
    val items = reader.readLine()
    val operation = reader.readLine()
    val test = reader.readLine()
    val ifTrue = reader.readLine()
    val ifFalse = reader.readLine()
    val last = reader.readLine()

    val arraySeq = mutable.ArraySeq(test, ifTrue, ifFalse)
    monkeys += Monkey.parse(monkey, items, operation, arraySeq)
    monkeys2 += Monkey.parse(monkey, items, operation, arraySeq)

    if last == null then
      guard = false
  end while

  // Modulo arithmetic black magic shit wtf
  modulo = monkeys.map(_.test.by).product

  for _ <- 1 to 20 do
    cycle(monkeys, true)
  for _ <- 1 to 10000 do
    cycle(monkeys2)

  List(monkeys, monkeys2).map(_.map(_.inspections).sorted(Ordering.Long.reverse).take(2).product).foreach(println)
end main
