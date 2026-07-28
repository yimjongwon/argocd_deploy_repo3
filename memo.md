### jenkins 플러그인 설치: generic webhook trigger
> 소스코드/배포 코드 같이있을 경우 사용
> pipeline->configure->generic webhook trigger->post 파라미터 추가
> Variable: COMMIT_MSG
> Expression: $.commits[0].message
> Token: my-token
> Optional filter
> ^((?!\[ci skip\])[\s\S])*$
> Text $COMMIT_MSG
> 깃허브 웹훅 수정
> https://jenkins.cloudflareyim.store/generic-webhook-trigger/invoke?Token=my-token