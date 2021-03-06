package day02;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.JTextField;


// MyFrame02
// JLabel -> 2 lbl
// Jbutton -> btn increase
// click event => lbl++
public class MyFrame02 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame02 frame = new MyFrame02();
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
	public MyFrame02() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("1");
		lbl.setBounds(88, 113, 57, 15);
		contentPane.add(lbl);
		
		JButton btn = new JButton("Click");
		tf = new JTextField();
		tf.setText("2");
		
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String cnt = lbl.getText();
				int int_cnt = Integer.parseInt(cnt);
				int_cnt++;
				lbl.setText(String.valueOf(int_cnt));
				
				String tf_btn = tf.getText();
				int int_tf_btn = Integer.parseInt(tf_btn);
				int_tf_btn++;
				tf.setText(String.valueOf(int_tf_btn));
			}
		});
		btn.setBounds(171, 109, 97, 23);
		contentPane.add(btn);
		
		tf.setBounds(74, 149, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
	}
}
