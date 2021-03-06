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

public class MyFrame03 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame03 frame = new MyFrame03();
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
	public MyFrame03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("+");
		lbl.setBounds(81, 114, 57, 15);
		contentPane.add(lbl);
		
		tf1 = new JTextField();
		tf1.setText("1");
		tf1.setBounds(12, 111, 57, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		tf2 = new JTextField();
		tf2.setText("2");
		tf2.setBounds(91, 111, 57, 21);
		contentPane.add(tf2);
		tf2.setColumns(10);
		
		JButton btn = new JButton("=");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String a = tf1.getText();
				String b = tf2.getText();
				int int_a = Integer.parseInt(a);
				int int_b = Integer.parseInt(b);
				
				int int_c = int_a + int_b;
				String c = String.valueOf(int_c);
				
				tf3.setText(c);
			}
		});
		btn.setBounds(178, 110, 65, 23);
		contentPane.add(btn);
		
		tf3 = new JTextField();
		tf3.setBounds(255, 111, 116, 21);
		contentPane.add(tf3);
		tf3.setColumns(10);
	}
}
