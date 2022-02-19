# mssql index 사용하기

-   실제 업무를 할 때 index를 생성하고 작업하는 것이 효율적인지, 그냥 하면 좋은지 가늠이 안 됨. 이하 정리로 해당 고민을 종결할 수 있을 예정 #mssql
-   결론, delete가 거의 없는 데이터는 계속 쌓아놓고, select를 분석에서 많이 사용하기 때문에 index를 적극적으로 활용해야 겠다. 하지만, 평소 분석, 추출 작업에서 임시로 쓰는 테이블들은 굳이 index 설정할 필요 없겠음, db 공간도 차지하고, 작은 테이블이 많기 때문에 불필요 할 듯, 실제 작업에서 큰 데이터는 hive sql 쪽에서 작업하는 경우가 많으니,,, 일단 평소 작업에서 index를 적극 활용하지는 않을 거 같음. (물론 아닐 수 있음,, 추후 갱신될 수 있음.)
<br>
-   Index란?
    -   테이블의 데이터를 조회할 때 빠르고 효과적으로 조회할 수 있도록 도와주는 역할을 함.
    -   select 할 때는 빠르지만 insert, update 수행 때는 느려지기 때문에 조회가 많은 테이블을 기준으로 설정해야 함. 
<br>
-   mssql index 생성 방법 (중복 허용)  

    ```
    CREATE INDEX [인덱스명] ON [테이블명] ([컬럼명] [정렬기준])
    ```


-   mssql unique index 생성 방법 (중복 비허용)  

    ```
    CREATE UNIQUE INDEX [인덱스명] ON [테이블명] ([컬럼명] [정렬기준])
    ```


-   예제 생성 1 - 테이블 생성 
    -   create table     

        ```
        CREATE TABLE work_ttt.dbo.성적표 (
            학생번호 int not null,
            학생이름 varchar(10) not null,
            점수 int not null
        )
        ```

    -   insert table    

        ```
        insert into wrok_ttt.dbo.성정표 (학생번호, 학생이름, 점수) values (1,'우왁굳',100)
        insert into wrok_ttt.dbo.성정표 (학생번호, 학생이름, 점수) values (2,'주르르',70)
        insert into wrok_ttt.dbo.성정표 (학생번호, 학생이름, 점수) values (3,'뢴트게늄',95)
        insert into wrok_ttt.dbo.성정표 (학생번호, 학생이름, 점수) values (4,'히키킹',95)
        ```

    -   select table   

        ```
        select * from work_ttt.dbo.성적표
        ```


-   예제 생성 2 - 인덱스 생성 
    -   성적표에서 점수로 인덱스를 설정하시오.   
        , 성적표의 점수는 중복될 수 있는 값임으로 중복 허용 index 생성 
    -   create index   

        ```
        create index value_index on work_ttt.dbo.성적표 (점수 asc)
        ```

         
    -   select index  

        ```
        select count(name) as 결과 from sys.indexes where name = 'value_index' -- 1
        ```

         
<br><br>
- 예제봐도, 궁금증이 해결되지 않네,, 다른 블로그 하나 더 참고함. 
<br>
-   인덱스 장점과 단점 
    -   장점 
        -   테이블을 조회하는 속도와 그에 따른 성능을 향상시킬 수 있다. 
        -   전반적인 시스템의 부하를 줄일 수 있다. 
    -   단점 
        -   인덱스를 관리하기 위해 DB의 약 10%에 해당하는 저장공간이 필요하다. 
        -   인덱스를 관리하기 위해 추가 작업이 필요하다. 
        -   인덱스를 잘못 사용할 경우 오히려 성능이 저하되는 역효과가 발생할 수 있다. 
    -   만약 create, delete, update가 빈번한 속성에 인덱스를 걸게되면 인덱스의 크기가 비대해져서 성능이 오히려 저하되는 역효과가 발생할 수 있다. 그러한 이유 중 하나는 delete와 update 연산 때문이다. update와 delete는 기존의 인덱스를 삭제하지 않고 '사용하지 않음' 처리를 한다. 만약 어떤 테이블에 update와 delete가 빈번하게 발생된다면 실제 데이터는 10만 건이지만 인덱스는 100만 건이 넘어가게 되어, sql문 처리시 비대해진 인덱스에 오히려 성능이 저하될 것이다. 
<br>
-   인덱스를 사용하면 좋은 경우 
    -   규모가 작지 않은 테이블 
    -   insert, update, delete가 자주 발생하지 않는 컬럼 
    -   join이나 where 또는 order by에 자주 사용되는 컬럼 
    -   데이터의 중복도가 낮은 컬럼  

        인덱스를 사용하는 것 만큼이나 생성된 인덱스를 관리해주는 것도 중요하다. 그렇기 때문에 사용하지 않는 인덱스는 바로 제거를 해줘야 한다. 

<br><br>

-   참고링크 
    -   https://kjhgao.tistory.com/138?category=997967
