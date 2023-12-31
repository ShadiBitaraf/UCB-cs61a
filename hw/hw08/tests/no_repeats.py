test = {
  'name': 'no-repeats',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (no-repeats '(5 4 3 2 1))
          2cd8b7f491d49051fe3a86c912bff438
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (no-repeats '(5 4 3 2 1 1))
          2cd8b7f491d49051fe3a86c912bff438
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (no-repeats '(5 5 4 3 2 1))
          2cd8b7f491d49051fe3a86c912bff438
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (no-repeats '(12))
          0987f17f42b47ec069f680a50c44ae4e
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (no-repeats '(1 1 1 1 1 1))
          4fbb2195709ce6677a192b31dd920a41
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (no-repeats (list 5 4 2))
          (5 4 2)
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (no-repeats (list 5 4 5 4 2 2))
          (5 4 2)
          scm> (no-repeats (list 5 5 5 5 5))
          (5)
          scm> (no-repeats ())
          ()
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
