; #2 over-or-under
(define (over-or-under num1 num2)
  (cond 
    [(< num1 num2)      -1]
    [(equal? num1 num2) 0]
    [(> num1 num2)      1]))

; (define (over-or-under num1 num2) (if (< num1 num2) -1)[(if equal? num1 num2) 0] else [(if (> num1 num2) 1)])
; #3 make adder
(define (make-adder num)
  (define (inner inc) (+ num inc))
  inner)

; (define (make-adder num)
;  (lambda (inc) (+ num inc))) ;with define has same issue as 3. thinks inner is string.

; #4 composed
(define (composed f g) (lambda (x) (f (g x))))

; #5 Make a List
(define lst
        (cons (cons 1 nil)
              (cons 2 (cons (cons 3 (cons 4 nil)) (cons 5 nil)))))

; #6 Remvove, optional
(define (remove item lst) 'YOUR-CODE-HERE)
