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

public class MyFrame07 extends JFrame {

	private JPanel contentPane;
	private JTextField tfCom;
	private JTextField tfMine;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame07 frame = new MyFrame07();
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
	public MyFrame07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblCom = new JLabel("컴 : ");
		lblCom.setBounds(12, 10, 57, 15);
		contentPane.add(lblCom);
		
		JLabel lblMe = new JLabel("나 : ");
		lblMe.setBounds(12, 49, 57, 15);
		contentPane.add(lblMe);
		
		tfCom = new JTextField();
		tfCom.setBounds(81, 7, 116, 21);
		contentPane.add(tfCom);
		tfCom.setColumns(10);
		
		tfMine = new JTextField();
		tfMine.setBounds(81, 46, 116, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		JLabel lblResult = new JLabel("결과 : ");
		lblResult.setBounds(12, 85, 57, 15);
		contentPane.add(lblResult);
		
		tfResult = new JTextField();
		tfResult.setBounds(81, 82, 116, 21);
		contentPane.add(tfResult);
		tfResult.setColumns(10);
		
		JButton btn = new JButton("실행하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myexecute();
			}
		});
		btn.setBounds(12, 131, 185, 23);
		contentPane.add(btn);
	}
	public void myexecute() {
		// 홀짝
		String me = tfMine.getText();
		double com_rnd = Math.random();
		String com = "";
		if(com_rnd < 0.5) {
			com = "홀";
		}else {
			com = "짝";
		}
		
		tfCom.setText(com);
		if(me.equals(com)) {
			tfResult.setText("승리");
		}else {
			tfResult.setText("패배");
		}
	}

}
