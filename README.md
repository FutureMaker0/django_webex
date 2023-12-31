# django_webex (django 기반 기술 블로그 개발)
  - 주제: 명언 공유 쉼터 커뮤니티


# 모델링 및 개발을 위한 간단한 내용정리
- blog
  ### models (views)
    - Post (C, R, U, D)
    - Comment (C, R, D)
    - Hashtag (C, R, D)
    --> 댓글과 해시태그는 포스트에 1:N 관계로 종속 (Foreign key)

- user
  ### models (views)
    - UseManager
    - User 
      - Registration
          - user
          - superuser
      - login 
      - logout 


# 유저 인증 및 이후 절차에 관한 유의사항
  - 로그인이 되지 않았을 때
    - blog/list 페이지 진입 시
        - 미로그인 상태 인지용 텍스트 노출
        - 게시글 작성 버튼 클릭 시 로그인 페이지로 전환
        - 전체 리스트 및 특정 포스트 내용을 확인은 가능
        - 포스트/댓글/해시태그에 대한 수정 및 삭제 등 조작 불가

  - 로그인이 되었을 때,
    - 화면 최상단 로그인 되었음을 나타내는 문구 노출 (username, 본 프로젝트에서는 email or nickname)
    - 본인이 작성한 글에 대해서만 수정, 삭제 가능 -> 타 계정 작성글에 대해서는 권한 없음으로 수정, 삭제 불가
    - 본인이 작성한 댓글, 해시태그에 대해서만 삭제 가능 -> 타 계정 등록 컨텐츠에 대해서는 권한 없음으로 삭제 불가
      (단, 본인이 작성한 포스트일 필요는 없음. 타 계정 작성글이라도 본인이 작성한 댓글/해시태그라면 삭제 가능)
  

#
<img width="947" alt="기술블로그 ER Diagram" src="https://github.com/FutureMaker0/django_webex/assets/120623320/6cf11cb6-b76f-406a-8f8f-3cee291e2804">


# 개발 요구사항 (3단계 기준, 2단계 달성)
|순번|내용|개발완료|
|----|-----|-----|
|1|메인페이지 구현||
||페이지 제목과 블로그 입장하기 버튼이 있습니다. |O|
||회원가입/로그인 버튼이 있습니다. |O|
||회원가입 버튼을 클릭하면 회원가입 페이지로 이동합니다.|O|
||로그인 버튼을 클릭하면 로그인 페이지로 이동합니다.|O|
|2|회원가입 기능 구현||
||회원가입을 할 수 있는 페이지가 있어야합니다.|O|
||입력받는 값은 id, password입니다.|O|
||<img width="1440" alt="user_register" src="https://github.com/FutureMaker0/django_webex/assets/120623320/dac32cc9-b2b7-46a7-8ce4-4c8beecc89f7">||
|3|로그인 기능 구현||
||로그인을 할 수 있는 페이지가 있어야합니다.|O|
||<img width="1440" alt="user_login" src="https://github.com/FutureMaker0/django_webex/assets/120623320/b6bb4484-2a6b-43d5-9204-9487c05671e8">||
||입력받는 값은 id, password입니다.|O|
||<img width="1440" alt="스크린샷 2023-07-20 오후 7 05 16" src="https://github.com/FutureMaker0/django_webex/assets/120623320/9c57745d-c859-4c5c-a116-3f989b5abaf0">||
|4|**게시글 작성 기능 구현**||
||로그인을 한 유저만 해당 기능을 사용 할 수 있습니다.|O|
||게시글 제목과 내용을 작성 할 수 있는 페이지가 있어야합니다.|O|
||작성한 게시글이 저장되어 게시글 목록에 보여야 합니다.|O|
||**사진 업로드가 가능하도록 합니다.**|X -> O|
||**첨부파일 다운로드가 가능하도록 합니다.**|X -> O|
||**게시글 조회수가 올라갈 수 있도록 합니다.**|X|
||<img width="1440" alt="post_form" src="https://github.com/FutureMaker0/django_webex/assets/120623320/0470a002-8127-4057-b754-5bde5a155e68">||
|5|게시글 목록 기능 구현||
||모든 사용자들이 게시한 블로그 게시글들의 제목을 확인 할 수 있습니다.|O|
||**게시글 내용 ... 축약을 통한 가독성 확보**|X -> O|
||<img width="1440" alt="post_list" src="https://github.com/FutureMaker0/django_webex/assets/120623320/6201fd49-f490-45b9-a630-d8026e680fa4">||
|6|게시글 상세보기 기능 구현||
||게시글의 제목/내용을 보는 기능입니다.|O|
||**게시글 작성 시 첨부된 파일 다운로드 기능. 파일 확장자에 따라 별도 아이콘 이미지 표기 (xlsx/word/csv/else)**|O|
||<img width="1440" alt="post_detail_image" src="https://github.com/FutureMaker0/django_webex/assets/120623320/78addb93-ac58-47c0-b635-c925e9535050">|첨부된 사진이 있는 경우의 상세보기 페이지|
||<img width="1440" alt="post_detail_noimage" src="https://github.com/FutureMaker0/django_webex/assets/120623320/7111df68-b29e-403b-9d2e-fc909f7cd64a">|첨부된 사진이 없는 경우의 상세보기 페이지|
|7|게시글 검색 기능 구현||
||주제와 태그에 따라 검색이 가능하게 합니다.|▲|
||검색한 게시물은 시간순에 따라 정렬이 가능해야 합니다.|▲|
||**카테고리 선택에 따른 검색목록 리스트업.**|O|
||<img width="1440" alt="selected_by_category1" src="https://github.com/FutureMaker0/django_webex/assets/120623320/c204fa86-4d10-463d-89db-37a6c41fa608">|카테고리1 검색|
||<img width="1440" alt="selected_by_category2" src="https://github.com/FutureMaker0/django_webex/assets/120623320/75fff418-7441-43d0-9460-dcb8ef21c0db">|카테고리2 검색|
|8|게시글 수정 기능 구현||
||로그인을 한 유저만 해당 기능을 사용 할 수 있습니다.|O|
||본인의 게시글이 아니라면 수정이 불가능합니다.|O|
||게시글의 제목 또는 내용을 수정 하는 기능입니다.|O|
||삭제를 완료한 이후에 게시글 목록 화면으로 돌아갑니다.|O|
||수정된 내용은 게시글 목록보기/상세보기에 반영되어야합니다.|O|
|9|게시글 삭제 기능 구현||
||로그인을 한 유저만 해당 기능을 사용 할 수 있습니다.|O|
||본인의 게시글이 아니라면 수정이 불가능합니다.|O|
||게시글을 삭제하는 기능입니다.|O|
||삭제를 완료한 이후에 게시글 목록 화면으로 돌아갑니다.|O|
||삭제된 게시글은 게시글 목록보기/상세보기에서 접근이 불가능하며, 접근 시도 시 <존재하지 않는 게시글입니다> 라는 페이지를 보여줍니다.|X|
|10|**회원 관련 추가 기능(UI 직접 구현 필요)**||
||비밀번호 변경기능|X|
||프로필 수정|X|
||닉네임 추가|O|
|11|**댓글 기능(UI 직접 추가 구현 필요)**||
||댓글 추가|O|
||댓글 삭제|O|
||대댓글|X|
|12|부가 기능||
||정적 파일 모으기 (collectstatic)|X|
||번역 기능 (en, kr)|X|
||댓글갯수 표기|O|
||**게시글 리스트 페이징**|O|
||<img width="1440" alt="스크린샷 2023-07-20 오후 7 08 00" src="https://github.com/FutureMaker0/django_webex/assets/120623320/79acbd6d-5a84-40ca-a9c9-230c01e39d57">||
|13|**AWS Lightsail 배포**||
||배포 및 운영, 서버 운영에 따른 비용이 청구 가능|X|


# 추가구현 예정
  - 프로필 모델 추가 및 기능추가(비밀번호 변경)
  - 메인 인덱스페이지 최신포스팅 완성
  - 이미지 업로드 (7.24 추가구현 완료)
  - 조회수 카운팅
  - 카테고리 완성 (7.25 추가구현 완료)

