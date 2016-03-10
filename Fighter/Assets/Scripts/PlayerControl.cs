using UnityEngine;
using System.Collections;

public class PlayerControl : MonoBehaviour {

	Animator anim;

	public float maxspeed = 1f;
	bool grounded = false;
	bool punched = false;
	int hp;
	public static int enhp;

	public Transform groundCheck;
	float groundRadius = 3.5f;
	public LayerMask whatIsGround;
	public Transform punchCheck;
	float punchRadius = 4f;
	public LayerMask whatIsPunch;

	// Use this for initialization
	void Start () {
		hp = 100;
		enhp = 100;
		anim = GetComponent<Animator> ();
	}

	void Update(){
		hp = Player2Control.enhp;
		if (hp == 0) {
			GetComponent<Rigidbody2D>().position = new Vector3(100,100,0);
		}
		if (punched && Input.GetKeyDown (KeyCode.Space)) {
			anim.SetBool("Punch", false);
			enhp -= 10;
		}
		if (grounded && Input.GetKeyDown (KeyCode.W)) {
			anim.SetBool("Ground", false);
			GetComponent<Rigidbody2D>().velocity = new Vector2(GetComponent<Rigidbody2D>().velocity.x, maxspeed);
		}
		if (Input.GetKeyDown (KeyCode.A)) {
			GetComponent<Rigidbody2D>().velocity = new Vector2(maxspeed*-1, GetComponent<Rigidbody2D>().velocity.y);
		}
		if (Input.GetKeyDown (KeyCode.D)) {
			GetComponent<Rigidbody2D>().velocity = new Vector2(maxspeed, GetComponent<Rigidbody2D>().velocity.y);
		}
	}
	
	// Update is called once per frame
	void FixedUpdate () {
		grounded = Physics2D.OverlapCircle (groundCheck.position, groundRadius, whatIsGround);
		anim.SetBool ("Ground", grounded);
		punched = Physics2D.OverlapCircle (punchCheck.position, punchRadius, whatIsPunch);
		anim.SetBool ("Punch", punched);
	}


}
