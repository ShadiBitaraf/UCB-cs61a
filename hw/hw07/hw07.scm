(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

; second 
(define (caddr s) (car (cdr (cdr s))))

; third
; (define (ordered? s) (cond (and (<= (car s) (car (cdr s)) (or (equal? (length s) 1) (equal? (length s) 0)))) #t #f))
(define (ordered? s)
  (cond 
    ((or (equal? (length s) 1) (equal? (length s) 0))
     #t)
    ((<= (car s) (car (cdr s)))
     (ordered? (cdr s)))
    (else
     #f)))

(define (square x) (* x x))

(define (pow base exp) ; both ints
  (if (or (= base 1) (zero? exp))
      1
      (if (even? exp)
          (square (pow base (/ exp 2)))
      (* (pow base (- exp 1)) base))))
