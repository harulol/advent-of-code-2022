(require 'clojure.string)
(def lines (clojure.string/split-lines (slurp "input.txt")))

(def expressions (atom {}))
(def monkeys (atom {}))

(defn split [str]
  (clojure.string/split str #" "))

(defn parse-monkeys []
  (doseq [line lines]
    (let [arr (clojure.string/split line #": ")]
      (if (= (count (split (get arr 1))) 1)
        (swap! monkeys assoc (get arr 0) (Integer/parseInt (get arr 1)))
        (swap! expressions assoc (get arr 0) (get arr 1))))))

(defn evaluate [left operand right]
  (cond
    (= operand "+") (+ left right)
    (= operand "-") (- left right)
    (= operand "*") (* left right)
    (= operand "/") (/ left right)
    :else (throw (Error. "Fuck"))))

(defn do-expression [monkey]
  (if (contains? @monkeys monkey)
    (get @monkeys monkey)
    (let [expression (split (get @expressions monkey)) left (get expression 0) operand (get expression 1) right (get expression 2)]
      (evaluate (do-expression left) operand (do-expression right)))))

(parse-monkeys)
(println (do-expression "root"))
