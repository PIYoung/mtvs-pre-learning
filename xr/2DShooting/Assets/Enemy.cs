using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Enemy : MonoBehaviour
{
  // - 방향
  Vector3 dir;
  // - 속력
  public float speed = 5;
  // Start is called before the first frame update
  void Start()
  {
    // 태어날 때 
    // 30% 확률로 플레이어 방향, 나머지 확률로 아래방향으로 정하고
    int result = UnityEngine.Random.Range(0, 10);
    if (result < 3)
    {
      // 플레이어 방향
      GameObject target = GameObject.Find("Player");
      // dir = target - me
      dir = (target.transform.position - transform.position);
      dir.Normalize();
    }
    else
    {
      // 아래방향
      dir = Vector3.down;
    }
  }

  // Update is called once per frame
  void Update()
  {
    // 살아가면서 그 방향으로 계속 이동하고싶다.
    transform.position += dir * speed * Time.deltaTime;
  }

  private void OnCollisionEnter(Collision other)
  {
    // 너죽고
    Destroy(other.gameObject);
    // 나죽자
    Destroy(gameObject);
  }
}
