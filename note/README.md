+++
title = "全部はできなかったがなるべくCDKでS3 Object Lambdaを作った"
date = "2021-03-28"
tags = ["S3 Object Lambda", "Lambda"]
+++

![img](/img/2021/04/cdks3objectlambda.png)

S3 Object LambdaをCDKで立ち上げようと思った。

というのも先週あたりに[AWS BlogでS3 Object Lambda](https://aws.amazon.com/blogs/aws/introducing-amazon-s3-object-lambda-use-your-code-to-process-data-as-it-is-being-retrieved-from-s3/)を見て一体何が便利なんだろう、と思っていたけど今日になって急に使いたいシーンを思いついたため。

そこで前述の記事を読みながら作ってみていたんだけれども、作っている途中でなんで動かないの？とひっかかるところがあった。

例えばこういうところ

* LambdaのデフォルトのPythonのboto3ライブラリが古くて使えない。（あくまで現時点（2021-03-28）でのこと）
* LambdaのIAMロールで`s3-object-lambda:WriteGetObjectResponse`を許可する必要がある

こうしたつまづきポイントに加えて、マネジメントコンソールでの操作なんて全然覚えていられないし、やはりCDKで作っておくべきだろうと思って取り掛かった。

作ってみてわかったけど、残念なことに現時点（CDK Version 1.95.1）の[@aws-cdk/aws-s3objectlambda](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-s3objectlambda-readme.html)ではハイレベルコンストラクトがなく、私のスキルではそこをコードにすることができなかった。

というわけで出来上がったCDKプロジェクトは

* S3バケット
* Lambda
* Accesspoint

だけは`cdk deploy`でデプロイできるのだが、それだけだとS3 Object Lambdaは完成せず、このデプロイの後でマネジメントコンソールで**Lambdaアクセスポイント**を手動設定する必要がある。

もう一度まとめると、デプロイに必要なものは

1. [Githubのリポジトリ](https://github.com/suzukiken/cdks3objectlambda)のコードで`cdk deploy`
2. マネジメントコンソールでLambdaアクセスポイントの設定

2はこういう作業です。

![img](/img/2021/03/s3objectlambda-accesspoint-setting.gif)

いずれはCDKでLambdaアクセスポイントの作成ができるようになるのでしょう。その時にまたリポジトリを直そうと思います。

