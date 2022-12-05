import java.io.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    static class Instruction {

        public final int amount;
        public final int source;
        public final int destination;

        public Instruction(final int amount, final int source, final int dest) {
            this.amount = amount;
            this.source = source;
            this.destination = dest;
        }

        public String toString() {
            return String.format("Instruction{amount=%s,source=%s,dest=%s}", amount, source, destination);
        }

    }

    // Huge method to just read a file in 2 chunks.
    private static List<?>[] readFile() {
        final List<?>[] array = new List[2];

        try {
            final File file = new File("./input.txt");
            List<String> lines = new ArrayList<>();
            final Scanner scanner = new Scanner(file);

            while (scanner.hasNextLine()) {
                final String line = scanner.nextLine();

                if (line.length() == 0) {
                    array[0] = lines;
                    lines = new ArrayList<>();
                    continue;
                }

                lines.add(line);
            }

            array[1] = lines;
            scanner.close();
        } catch (final Exception exception) {
            exception.printStackTrace();
        }

        return array;
    }

    private static Map<Integer, String> parseDiagram(final List<String> list) {
        final Map<Integer, String> map = new HashMap<>(); // Map to return as a diagram. Col => String
        final Map<Integer, Integer> indices = new HashMap<>(); // Map to track boxes to draw diagram. Index => Col
        final Pattern pattern = Pattern.compile("\\[(\\w)\\]");

        // Block to find the columns with the indices to use later.
        // Idk why I'm making it so complicated.
        {
            final Pattern patt = Pattern.compile("(\\d+)");
            final String markup = list.remove(list.size() - 1);
            final Matcher matcher = patt.matcher(markup);

            while (matcher.find()) {
                final int columnNumber = Integer.parseInt(markup.substring(matcher.start(), matcher.start() + 1));
                indices.put(matcher.start(), columnNumber);
            }
        }

        // Go through the boxes line and find indices of the names of the boxes.
        list.forEach(line -> {
            final Matcher matcher = pattern.matcher(line);

            while (matcher.find()) {
                // Have to account for the first [ in [A], so +1.
                final int column = indices.get(matcher.start() + 1);
                final String box = line.substring(matcher.start() + 1, matcher.start() + 2);
                if (map.putIfAbsent(column, box) != null)
                    map.put(column, String.format("%s%s", box, map.get(column)));
            }
        });
        return map;
    }

    private static List<Instruction> parseInstructions(final List<String> list) {
        final List<Instruction> instructions = new ArrayList<Instruction>();
        final Pattern pattern = Pattern.compile("move (\\d+) from (\\d+) to (\\d+)");

        list.forEach(item -> {
            final Matcher matcher = pattern.matcher(item);
            matcher.find();

            final int amount = Integer.parseInt(matcher.group(1));
            final int source = Integer.parseInt(matcher.group(2));
            final int destination = Integer.parseInt(matcher.group(3));

            final Instruction instruction = new Instruction(amount, source, destination);
            instructions.add(instruction);
        });

        return instructions;
    }

    private static void execute(final Map<Integer, String> diagram, final Instruction instruction,
            final boolean reverse) {
        final String s = diagram.get(instruction.source);
        final String left = s.substring(0, Math.max(s.length() - instruction.amount, 0));
        final String move = s.substring(Math.max(s.length() - instruction.amount, 0));

        // Since we move from top one-by-one, we have to reverse the string, that's all
        // I think. If we move all in same order like part 2, reversing is unnecessary.
        final StringBuilder builder = new StringBuilder();
        builder.append(move);

        if (reverse)
            builder.reverse();

        diagram.put(instruction.source, left);
        diagram.put(instruction.destination, diagram.get(instruction.destination) + builder.toString());
    }

    private static void printTopBoxes(final Map<Integer, String> diagram) {
        diagram.forEach((i, s) -> System.out.printf("%s", s.substring(s.length() - 1)));
        System.out.println();
    }

    @SuppressWarnings("unchecked")
    public static void main(final String[] args) {
        final List<?>[] array = readFile();
        final Map<Integer, String> diagram1 = parseDiagram((List<String>) array[0]);
        final Map<Integer, String> diagram2 = new HashMap<>(diagram1);
        final List<Instruction> instructions = parseInstructions((List<String>) array[1]);

        instructions.forEach(instr -> execute(diagram1, instr, true)); // Part 1
        instructions.forEach(instr -> execute(diagram2, instr, false)); // Part 2
        printTopBoxes(diagram1);
        printTopBoxes(diagram2);
    }

}
