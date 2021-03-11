package day02;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyFrame08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_com;
	private JTextField tf_me;
	private JTextField tf_result;
	private JButton btn_r;
	private JButton btn_p;
	private JButton btn_s;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame08 frame = new MyFrame08();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MyFrame08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl_com = new JLabel("컴 : ");
		lbl_com.setBounds(12, 37, 57, 15);
		contentPane.add(lbl_com);
		
		JLabel lbl_me = new JLabel("나 :");
		lbl_me.setBounds(12, 62, 57, 15);
		contentPane.add(lbl_me);
		
		JLabel lbl_result = new JLabel("결과");
		lbl_result.setBounds(12, 87, 57, 15);
		contentPane.add(lbl_result);
		
		tf_com = new JTextField();
		tf_com.setBounds(81, 34, 116, 21);
		contentPane.add(tf_com);
		tf_com.setColumns(10);
		
		tf_me = new JTextField();
		tf_me.setBounds(81, 59, 116, 21);
		contentPane.add(tf_me);
		tf_me.setColumns(10);
		
		tf_result = new JTextField();
		tf_result.setBounds(81, 84, 116, 21);
		contentPane.add(tf_result);
		tf_result.setColumns(10);
		
		JButton btn = new JButton("실행");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
			}
		});
		btn.setBounds(12, 112, 97, 23);
		contentPane.add(btn);
		
		btn_r = new JButton("바위");
		btn_r.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf_me.setText("바위");
				execute();
			}
		});
		btn_r.setBounds(218, 58, 97, 23);
		contentPane.add(btn_r);
		
		btn_p = new JButton("보");
		btn_p.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf_me.setText("보");
				execute();
			}
		});
		btn_p.setBounds(218, 83, 97, 23);
		contentPane.add(btn_p);
		
		btn_s = new JButton("가위");
		btn_s.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf_me.setText("가위");
				execute();
			}
		});
		btn_s.setBounds(218, 33, 97, 23);
		contentPane.add(btn_s);
	}
	public void execute() {
		// 가위바위보
		String me = tf_me.getText();
		double com_rnd = Math.random();
		String com = "";
				
		if(com_rnd > 0.7) {
			com = "가위";
		}else if(com_rnd > 0.4){
			com = "바위";
		}else {
			com = "보";
		}
		
		tf_com.setText(com);
		if(me.equals(com)) {
			tf_result.setText("비겼다");
		}else if((me.equals("가위") && com.equals("보")) ||(me.equals("바위") && com.equals("가위")) ||(me.equals("보") && com.equals("바위")) ) {
			tf_result.setText("이겼다");
		}else {
			tf_result.setText("졌다");
		}
		
	}

}
