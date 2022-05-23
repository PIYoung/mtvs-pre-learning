using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyManager : MonoBehaviour
{
  // - 적 공장
  public GameObject enemyFactory;
  // - 현재시간
  float currentTime;
  // - 생성시간
  public float createTime = 1; // 1seconds
  // Start is called before the first frame update
  void Start()
  {

  }

  // Update is called once per frame
  void Update()
  {
    // 1. 시간이 흐르다가
    currentTime += Time.deltaTime;
    // 2. 만약 현재시간이 생성시간이되면
    if (currentTime > createTime)
    {
      // 3. 적 공장에서 적을 만들어서
      GameObject enemy = Instantiate(enemyFactory);
      // 4. 내 위치에 가져다 놓고싶다.
      enemy.transform.position = transform.position;
      // 5. 현재시간을 0으로 초기화 하고싶다.
      currentTime = 0;
    }
  }
}
