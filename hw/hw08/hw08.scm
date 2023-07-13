(define (my-filter func lst) 

(cond
  ((= (length lst) 0) '())  ;if list empty = ()

  ((func (car lst))(cons (car lst) (my-filter func (cdr lst)))) ;elif meets predicate. how do i call func? how do update my list

  (else (my-filter func (cdr lst))) ;else, return an empty list

  )
)

(define (interleave s1 s2) 
(cond
  ((null? s1) s2) ;base case
  ((null? s2) s1);base case
  ((cons (car s1) (cons (car s2) (interleave (cdr s1) (cdr s2)))))
))


(define (accumulate merger start n term)
              ;func 2para,1st int, num of ints, func 1para
; base case: how do you know youve reached the end?
; merge terms together w merger

(if (<= n 0) start ;decrememnt n and check if we reached the end 

(merger (term n)(accumulate merger start (- n 1) term))
)
)


(define (no-repeats lst) 'YOUR-CODE-HERE)
