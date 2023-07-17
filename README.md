# django_webex

# blog app
  # models (views)
    - Post (create O, update O, delete O)
    - Comment (write O, delete O)
    - Hashtag (write O, delete O)
    --> 댓글과 해시태그는 포스트에 1:N 관계로 종속 (Foreign key)
  
===== updated at 0713 =====

# user app
  # models (views)
    - UseManager
    - User 
      - Registration O
          - user
          - superuser
      - login 
      - logout 

===== updated at 0714 =====

# Things to be aware of regarding user authentication and subsequent procedures
  # 로그인이 되지 않았을 때,
    - blog/list 페이지 진입 시, 미로그인 상태임 인지용 문구 노출, 게시글 작성 버튼 클릭 시 로그인 페이지로 전환
    - 전체 리스트 및 특정 포스트 내용을 확인할 수는 있으나, 포스트/댓글/해시태그에 대한 수정 및 삭제 등 조작 불가

  # 로그인이 되었을 때,
    - 화면 최상단 로그인 되었음을 나타내는 문구 노출 (username, 본 프로젝트에서는 email)
    - 본인이 작성한 글에 대해서만 수정, 삭제 가능 -> 타 계정 작성글에 대해서는 권한 없음으로 수정, 삭제 불가
    - 본인이 작성한 댓글, 해시태그에 대해서만 삭제 가능 -> 타 계정 등록 컨텐츠에 대해서는 권한 없음으로 삭제 불가
      (단, 본인이 작성한 포스트일 필요는 없음. 타 계정 작성글이라도 본인이 작성한 댓글/해시태그라면 삭제 가능)

===== updated at 0717 =====
