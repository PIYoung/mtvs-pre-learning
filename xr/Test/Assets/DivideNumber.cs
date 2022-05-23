using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DivideNumber : MonoBehaviour
{
  // Start is called before the first frame update
  void Start()
  {
    int n = 512;
    int answer = 0;

    while (true)
    {
      // 1. n을 나눈 나머지값을 answer에 저장한다.
      answer += n % 10;
      // 2. n을 나눈 몫을 n에 다시 넣는다.
      n = n / 10;
      // 3. 만약에 n이 0이면 반복문을 멈춘다.
      if (n == 0) break;
    }

    // 4. 결과를 출력한다.
    print(answer);
  }

  // Update is called once per frame
  void Update()
  {

  }
}
