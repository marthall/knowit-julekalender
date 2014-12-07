
(defn multiplication-table ([x]
    (for [i (range 1 (+ x 1))
          j (range i (+ x 1))]
          (* i j))))

(println (count (set (multiplication-table 8000))))