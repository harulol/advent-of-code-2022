import java.io.File
import kotlin.math.abs

fun checkCycle(register: Int, cycle: Int): Int {
    return if((cycle - 20) % 40 == 0) {
        cycle * register
    } else 0
}

fun main() {
    val lines = File("./input.txt").readLines()

    var register = 1
    var cycle = 1
    var strength = 0

    val pixels = mutableSetOf<Int>()

    fun incrementCycle(count: Int = 1) {
        repeat(count) {
            // Drawing the pixel.
            var position = cycle
            while(position > 40) position -= 40
            position-- // Index version.

            if(abs(register - position) <= 1)
                pixels.add(position)

            if(cycle % 40 == 0) {
                println(String(arrayOfNulls<Char>(40).mapIndexed { i: Int, _ -> if(i in pixels) '#' else '.' }.toCharArray()))
                pixels.clear()
            }

            // Then, calculate the strength.
            strength += checkCycle(register, cycle++)
        }
    }

    // Part one.
    var i = 0
    while(true) {
        if(i >= lines.size)
            break

        if(lines[i] == "noop") {
            incrementCycle()
        } else {
            val value = lines[i].split(" ")[1].toInt()

            // Addx takes 2 cycles to complete.
            incrementCycle(2)
            register += value
        }

        i++
    }

    println(strength)
}
