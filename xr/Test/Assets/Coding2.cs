using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Coding2 : MonoBehaviour
{
  int Plus(int a, int b)
  {
    result = 100;
    return a + b;
  }

  int result;

  // Start is called before the first frame update
  void Start()
  {
    int result = Plus(10, 20);
    print(this.result);
  }

  // Update is called once per frame
  void Update()
  {

  }
}
