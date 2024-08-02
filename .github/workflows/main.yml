name: Pull_test
on: workflow_dispatch
jobs:
  docker_pull:
    name: 拉取镜像打包测试
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    - run: pip install aligo
    - run: mkdir dockerimages
    - run: cd dockerimages
    - run: echo $(pwd)
