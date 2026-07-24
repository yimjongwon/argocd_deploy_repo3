### 앱이 실행되는지 확인하기위한 pod 접속,curl 테스트
```bash
k get pod -o wide
NAME                                 READY   STATUS    RESTARTS       AGE     IP                NODE    NOMINATED NODE   READINESS GATES
hello-app-fortune-64679c77cb-jmcwd   1/1     Running   0              2m35s   192.168.166.151   node1   <none>           <none>
hello-app-greet-68c869668d-9h7l9     1/1     Running   0              2m35s   192.168.166.154   node1   <none>           <none>

kubectl run netshoot --rm -i --tty --image nicolaka/netshoot -- /bin/bash


curl 192.168.166.151:8000/fortune
curl 192.168.166.154:8000/greet
```